import streamlit as st
import getpass
import os

st.title("🦜🔗 Quickstart App")

# Load environment variables if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

os.environ["LANGSMITH_TRACING"] = "true"

from langchain_ollama import ChatOllama

def generate_response(input_text):
    llm = ChatOllama(
        model="llama3.2:1b",
        temperature=0.8,
        num_predict=256,
    )
    response = llm.invoke(input_text)
    st.markdown(f"{response.content}")

with st.form("my_form"):
    text = st.text_area("Enter text:")
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)

