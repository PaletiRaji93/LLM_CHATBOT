from langchain.openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser  



from streamlit as st
import os
from dotenv import load_dotenv


os.environ["OPENAI_API_KEY"] = "sk-..." 
#langsmith tracking 
os.environ["LANGCHAIN_API_KEY"] = "langchain-api-key"  # Replace with your actual LangChain API key
os.environ["LANGCHIAN_TRACING_V2"] = "true"  # Replace with your actual LangChain project name


#prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant .Please response to the user queries"),
        ("user","Question:{question}")
    ]
)




#streamlit framework
st.title("LangChain Chatbot Demo with OPENAI API")
input_text=st.text_input("Search the topic you want")

#openAI LLm
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt | llm | output_parser
