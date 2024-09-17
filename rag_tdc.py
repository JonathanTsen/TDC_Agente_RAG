import os
import streamlit as st
import openai
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from openai import OpenAIError
from langchain_community.document_loaders import PyPDFLoader  # Importar a nova classe
from langchain.llms import OpenAI  # Adicionar esta linha

from dotenv import load_dotenv

load_dotenv()

# Configurar a chave da API do OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Função para carregar e processar o PDF usando PyPDFLoader
def load_pdf_with_pypdf_loader(pdf_file_path):
    loader = PyPDFLoader(pdf_file_path)
    documents = loader.load()
    return documents

# Função para dividir o texto dos documentos em chunks utilizáveis
def create_chunks(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)
    return chunks

# Função para realizar a busca e resposta com RAG
def get_rag_response(query, retriever):
    try:
        llm = OpenAI(temperature=0)
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff", 
            retriever=retriever
        )
        response = qa_chain.run(query)
        return response
    except OpenAIError as e:
        return f"Erro na API do OpenAI: {e}"

# Interface do Streamlit
def main():
    st.title("Assistente da Legislação Brasileira")

    # Upload do PDF
    pdf_file = st.file_uploader("Faça o upload do PDF com o Código do determinado ramo", type=["pdf"])

    if pdf_file is not None:
        # Salvar o PDF temporariamente para processamento
        with open("uploaded_pdf.pdf", "wb") as f:
            f.write(pdf_file.getbuffer())
        
        # Ler e processar o PDF usando PyPDFLoader
        documents = load_pdf_with_pypdf_loader("uploaded_pdf.pdf")
        st.write("PDF carregado com sucesso!")

        # Dividir o texto dos documentos em chunks
        chunks = create_chunks(documents)

        # Criar as embeddings dos chunks usando LangChain e FAISS
        embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
        knowledge_base = FAISS.from_documents(chunks, embeddings)

        # Configurar o retriever para o modelo de RAG
        retriever = knowledge_base.as_retriever(search_k=3)  # Buscar os 3 chunks mais relevantes

        # Input da pergunta do usuário
        user_question = st.text_input("Digite sua pergunta sobre o PDF")

        if user_question:
            # Gerar a resposta baseada na pergunta e nos chunks relevantes
            response = get_rag_response(user_question, retriever)
            st.write(f"Resposta: {response}")

if __name__ == "__main__":
    main()
