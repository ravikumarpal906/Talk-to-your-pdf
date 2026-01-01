import streamlit as st
import os
import tempfile
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
# NEW: TFIDF Retriever (No API needed, No Heavy Download)
from langchain_community.retrievers import TFIDFRetriever
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="Talk to PDF", page_icon="📄")
st.title("📄 AI Research Assistant (Lightweight)")

# PASTE YOUR KEY HERE
api_key = "AIzaSyCoxkU59EwZ7yrPZKqOOdKEKoXT4-6CTQc"
os.environ["GOOGLE_API_KEY"] = api_key

# --- 2. SIDEBAR ---
with st.sidebar:
    st.header("Upload Document")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    process_button = st.button("Process PDF")

if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None

# --- 3. PROCESSING (The "Brain") ---
if uploaded_file is not None and process_button:
    with st.spinner("Analyzing PDF using TF-IDF (Fast & Free)..."):
        try:
            # Save file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                tmp_path = tmp_file.name

            # Load & Split
            loader = PyPDFLoader(tmp_path)
            docs = loader.load()
            
            # Standard chunking
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=100)
            splits = text_splitter.split_documents(docs)

            # --- THE MAGIC SWITCH: TF-IDF ---
            # Instead of Vectors (which need API/GPU), we use Statistical Search.
            # It finds keywords in your PDF instantly.
            retriever = TFIDFRetriever.from_documents(splits)

            # --- CHAT CHAIN ---
            llm = ChatGoogleGenerativeAI(model="gemini-flash-latest", temperature=0.3)
            
            template = """Answer the question based only on the following context:
            {context}

            Question: {question}
            """
            prompt = ChatPromptTemplate.from_template(template)
            
            def format_docs(docs):
                return "\n\n".join(doc.page_content for doc in docs)

            st.session_state.rag_chain = (
                {"context": retriever | format_docs, "question": RunnablePassthrough()}
                | prompt
                | llm
                | StrOutputParser()
            )

            st.success(f"✅ Ready! Processed {len(splits)} chunks using TF-IDF.")
            os.remove(tmp_path)

        except Exception as e:
            st.error(f"Error: {e}")

# --- 4. CHAT ---
if st.session_state.rag_chain:
    st.divider()
    user_query = st.text_input("Ask a question about your PDF:")
    if user_query:
        with st.spinner("Thinking..."):
            try:
                response = st.session_state.rag_chain.invoke(user_query)
                st.write("### Answer:")
                st.write(response)
            except Exception as e:
                st.error(f"Error: {e}")