import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate



import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(
    Path(__file__).resolve().parent.parent / ".env",
    override=True
)

os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY", "")
os.environ["LANGSMITH_ENDPOINT"] = "https://apac.api.smith.langchain.com"
os.environ["LANGSMITH_PROJECT"] = "Ollama-Chatbot-Monitoring"
# Prompt
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful assistant. Please respond to the user's queries."
    ),
    (
        "user",
        "Question: {question}"
    )
])

# Ollama
llm = OllamaLLM(
    model="llama3.2"
)

# Chain
chain = prompt | llm

# Streamlit UI
st.title("LangChain Chatbot Demo with Llama 3.2")

input_text = st.text_input("Ask your question")

if input_text:
    with st.spinner("Thinking..."):
        response = chain.invoke({
            "question": input_text
        })

    st.write("### Response:")
    st.write(response)