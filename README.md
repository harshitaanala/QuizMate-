# QuizMate-Azure 🧠☁️  
Your AI-powered question generator from PDFs, built with Streamlit and Azure Cognitive Services. Upload any PDF document—whether it’s an academic paper, textbook, or corporate report—and get intelligently crafted quiz questions like MCQs, True/False, Fill-in-the-blanks, and Short Answer Questions, powered by Azure OpenAI. This tool eliminates the manual effort of reading and framing questions, making it ideal for educators, students, and professionals preparing learning material.

---

## 💡 About the Project

**QuizMate-Azure** is a lightweight web app that:
- 📄 Takes a **PDF** file as input
- 📚 Extracts **text** from the document
- 🤖 Uses **Azure AI (Text Analytics)** to analyze the content
- 📝 Generates **interactive quiz questions** like:
  - Multiple Choice Questions (MCQ)
  - True/False
  - Fill in the Blanks
  - Short Answer

Ideal for students, educators, and content creators who want to convert study material into quizzes with zero manual effort.

---

## 🚀 Features

- ✅ PDF Upload with real-time preview
- ✅ Text extraction from PDFs
- ✅ Option to generate:
  - MCQs
  - True/False questions
  - Fill in the Blanks
  - Short Answer questions
- ✅ Azure-based NLP — fast and reliable
- ✅ Simple and clean **Streamlit UI**
- ✅ Modular code — each feature works independently

---

## 🧱 Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **Cloud NLP API:** Azure AI - Text Analytics & Form Recognizer (via Azure Cognitive Services)
- **PDF Parsing:** Azure Document Intelligence

---

## 🧑‍💻 Setup Instructions

### 1. 🔧 Prerequisites

- Python 3.10+
- Azure account with free trial ([https://portal.azure.com](https://portal.azure.com))
- Azure Text Analytics Resource

### 2. 🌀 Clone the Repo

```bash
git clone https://github.com/your-username/QuizMate-Azure.git
cd QuizMate-Azure
