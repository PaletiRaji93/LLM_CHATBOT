import  requests  i
import streamlit as st


def get_openai_response(input_text):
    response=requests.post("http://localhost:8000/essay/invoke"),
    json={"input":{"topic":input_text}}
    return response.json()["output"]["content"]


def get_openai_response(input_text):
    response=requests.post("http://localhost:8000/poem/invoke"),
    json={"input":{"topic":input_text}}
    return response.json()["output"]

#streamlit framework

st.title('Langchain Demo with LLama3.2 API')
input_text=st.text_input("write an eassy on")
input_text1=st.text_input("write an poem on")

if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_openai_response(input_text))