# 📄 Talk to PDF: RAG-Based AI Research Assistant

## 📌 Project Overview

**Talk to PDF** is a Generative AI application that allows users to upload technical documents (PDFs) and ask questions in natural language. The system analyzes the document content and provides accurate, context-aware answers.

Unlike traditional LLM chatbots that *hallucinate* facts, this project uses a **Retrieval-Augmented Generation (RAG)** pipeline. It grounds the AI's responses strictly in the provided document, ensuring high accuracy for academic and professional use cases.

---

## 🚀 Key Features

- **Zero-Dependency Retrieval**  
  Uses **TF-IDF (Term Frequency–Inverse Document Frequency)** for sparse retrieval, eliminating the need for heavy vector databases or expensive embedding APIs.

- **High-Speed Processing**  
  Processes large PDFs in seconds on a standard CPU (laptop).

- **State-of-the-Art LLM**  
  Powered by **Google Gemini 1.5 Flash** for reasoning and answer synthesis.

- **Hallucination Control**  
  The system explicitly answers only from the provided document context.

- **User-Friendly Interface**  
  Built with **Streamlit** for a clean and responsive web UI.

---

## 🛠️ Tech Stack

| Component | Technology Used |
|---------|-----------------|
| Language | Python 3.12 |
| LLM (Generation) | Google Gemini 1.5 Flash |
| Retrieval Method | TF-IDF (Scikit-Learn) |
| Orchestration | LangChain (LCEL) |
| Frontend | Streamlit |
| PDF Processing | PyPDF |

---

## ⚙️ Installation & Setup

### 1. Prerequisite

You need a **Google Gemini API Key**.  
Get it for free from **Google AI Studio**.

---

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/talk-to-pdf.git
cd talk-to-pdf
```
### 3. Create a Virtual Environment

It is recommended to use a virtual environment to avoid dependency conflicts.

```bash
# Windows
python -m venv venv
venv\Scripts\activate


# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install streamlit langchain-google-genai langchain-community scikit-learn pypdf
```

## 🏃‍♂️ How to Run
1. Open the project folder in VS Code or Terminal.
2. Run the Streamlit server:

```bash
    streamlit run app.py
```
3. The application will open automatically in your browser at http://localhost:8501.
4. Paste your API Key in the code (line 18 of app.py) or keep it ready to enter if prompted.

## 🧠 Methodology (How it Works)
1. Ingestion: The user uploads a PDF. The system reads the file using PyPDFLoader.

2. Chunking: The text is split into smaller chunks (2000 characters) using ```RecursiveCharacterTextSplitter.```

3. Retrieval (TF-IDF): instead of converting text to heavy vectors, the system indexes the chunks using statistical keyword frequency. When a user asks a question, the system finds the most statistically relevant chunks.

4. Generation: The relevant chunks + the user question are sent to Gemini Flash, which formulates a human-like answer.