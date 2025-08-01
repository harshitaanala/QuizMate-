# QuizMate-Azure 🧠☁️  
Your AI-powered question generator from PDFs, built with Streamlit and Azure Cognitive Services. Upload any PDF document—whether it’s an academic paper, textbook, or corporate report—and get intelligently crafted quiz questions like MCQs, True/False, Fill-in-the-blanks, and Short Answer Questions, powered by Azure OpenAI. This tool eliminates the manual effort of reading and framing questions, making it ideal for educators, students, and professionals preparing learning material.

You can checkout the live application here : https://q4snfhavtjtvraxtwfl6my.streamlit.app/
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

## Screenshots

### 1) Main UI
<img width="959" height="426" alt="azure quiz app pic4" src="https://github.com/user-attachments/assets/8bf50b5e-21bc-4e14-9844-091e45cd45cd" />

### 2) Text Extracted
<img width="958" height="435" alt="azurequiz 1 pic" src="https://github.com/user-attachments/assets/79da4ea9-b839-4bc2-86a2-381e744bdbbe" />

### 3) Questions generated
<img width="959" height="433" alt="azure quiz app pic2" src="https://github.com/user-attachments/assets/b66742e2-33ef-45c1-a119-24428c518fce" />

### 4) Options to choose the type of questions
<img width="953" height="290" alt="azure quiz pic 5" src="https://github.com/user-attachments/assets/6b66726e-adec-44c6-b813-ca33c127ac60" />


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
