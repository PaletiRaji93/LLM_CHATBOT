from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

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
os.environ["LANGSMITH_PROJECT"] = "Google-Chatbot-Monitoring"

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY", "")
# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Please respond to the user's queries."
        ),
        (
            "user",
            "Question: {question}"
        )
    ]
)


# OpenAI LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",

)


# Output parser
output_parser = StrOutputParser()


# LangChain chain
chain = prompt | llm | output_parser


# Streamlit UI
st.title("LangChain Chatbot Demo with Google Gemini API")

input_text = st.text_input("Search the topic you want")


# Generate response
if input_text:
    with st.spinner("Thinking..."):
        response = chain.invoke(
            {
                "question": input_text
            }
        )

    st.write("### Response:")
    st.write(response)
