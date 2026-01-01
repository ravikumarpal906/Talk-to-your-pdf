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
