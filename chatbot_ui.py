import os
import streamlit as st
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

#streamlit run chatbot_ui.py

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "#"

# Define the chatbot function
def chatbot_response(query, file_path):
    # Load the local text file with UTF-8 encoding
    loader = TextLoader('C:\\Users\\Shivam\\OneDrive\\Desktop\\College\\Trimester-4\\NLP\\Project\\data.txt', encoding='utf-8')

    # Split the text into manageable chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    documents = loader.load_and_split(text_splitter=text_splitter)

    # Create OpenAI embeddings
    embeddings = OpenAIEmbeddings()

    # Create a FAISS vectorstore from the documents
    vectorstore = FAISS.from_documents(documents, embeddings)

    # Create the retrieval-based question-answering chain
    qa = RetrievalQA.from_chain_type(llm=OpenAI(temperature=0), chain_type="stuff", retriever=vectorstore.as_retriever())

    # Query the model
    result = qa.run(query)
    
    return result

# Streamlit UI components
st.title("🌟 LangChain Chatbot 🌟")
st.write("Ask a question based on the contents of your local text file.")

# File uploader
uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

if uploaded_file:
    st.write("File uploaded:", uploaded_file.name)
    
    # Input box for user query
    user_input = st.text_input("Enter your question:", "")

    # Button to submit the query
    if st.button("Ask"):
        if user_input:
            response = chatbot_response(user_input, uploaded_file)
            st.write("Response:", response)
        else:
            st.write("Please enter a question.")

