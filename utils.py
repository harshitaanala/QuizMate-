import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()


FORM_KEY = os.getenv("AZURE_FORM_KEY")
FORM_ENDPOINT = os.getenv("AZURE_FORM_ENDPOINT")
OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
OPENAI_MODEL = os.getenv("AZURE_OPENAI_MODEL")
OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")

def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a PDF file using Azure Form Recognizer
    Args:
        pdf_file: File-like object containing the PDF data
    Returns:
        str: Extracted text
    Raises:
        Exception: If extraction fails
    """
    url = f"{FORM_ENDPOINT}/formrecognizer/documentModels/prebuilt-read:analyze?api-version=2023-07-31"
    headers = {
        "Ocp-Apim-Subscription-Key": FORM_KEY,
        "Content-Type": "application/pdf"
    }
    response = requests.post(url, headers=headers, data=pdf_file)
    if response.status_code != 202:
        raise Exception(f"Form Recognizer error: {response.text}")
    
    result_url = response.headers["Operation-Location"]

    for _ in range(10):
        result = requests.get(result_url, headers={"Ocp-Apim-Subscription-Key": FORM_KEY})
        result_json = result.json()
        if result_json["status"] == "succeeded":
            structured_text = []
            for page in result_json["analyzeResult"]["pages"]:
                current_paragraph = []
                for line in page["lines"]:
                    current_paragraph.append(line["content"])
                    
                    if line["content"].strip().endswith('.'):
                        structured_text.append(" ".join(current_paragraph))
                        current_paragraph = []
                
                if current_paragraph:
                    structured_text.append(" ".join(current_paragraph))
            return "\n\n".join(structured_text)  
        time.sleep(2)

    raise Exception("Form Recognizer did not return result in time.")

def generate_questions(text, qtype="MCQ", num_questions=3):
    """
    Generates questions based on extracted text using Azure OpenAI
    Args:
        text: Extracted text content
        qtype: Type of questions to generate (MCQ, True/False, Fill in the Blanks, Short Answer)
        num_questions: Number of questions to generate (default: 3)
    Returns:
        str: Generated questions
    Raises:
        Exception: If question generation fails
    """
    prompt_map = {
        "MCQ": f"Generate {num_questions} multiple choice questions with 4 options each and indicate the correct answer. Base your questions strictly on the following text:\n\n",
        "True/False": f"Generate {num_questions} true or false questions. Base your questions strictly on the following text:\n\n",
        "Fill in the Blanks": f"Generate {num_questions} fill-in-the-blank questions. Base your questions strictly on the following text:\n\n",
        "Short Answer": f"Generate {num_questions} short answer questions (1-2 lines). Base your questions strictly on the following text:\n\n"
    }

    if qtype not in prompt_map:
        raise ValueError(f"Invalid question type. Supported types: {list(prompt_map.keys())}")

   
    MAX_TEXT_LENGTH = 3000  # characters
    if len(text) > MAX_TEXT_LENGTH:
        text = text[:MAX_TEXT_LENGTH]
        print(f"Warning: Text truncated to {MAX_TEXT_LENGTH} characters to fit token limits")

    prompt = prompt_map[qtype] + text

    headers = {
        "api-key": OPENAI_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful educational assistant that generates accurate questions based on provided text."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "max_tokens": 800 
    }

    url = f"{OPENAI_ENDPOINT}/openai/deployments/{OPENAI_DEPLOYMENT_NAME}/chat/completions?api-version={OPENAI_API_VERSION}"

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Error generating questions: {str(e)}")
        print(f"Response: {response.text if 'response' in locals() else 'No response'}")
        raise Exception(f"Failed to generate questions: {str(e)}")
