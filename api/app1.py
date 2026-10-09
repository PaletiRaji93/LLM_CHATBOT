from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_modules import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_ollama import OllamaLLM
from langchian-community.llms import Ollama
from dotenv import load_dotenv
load_dotenv()


os.environ["OPEN_API_KEY"]=os.getenv("OPENAI_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A Simple API Server"

)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"

)
model=ChatOpenAI()

llm = OllamaLLM(model="llama3.2")

prompt1=ChatPromptTemplate.form_template("write me an essay about {topic} with 100 words")

prompt2=ChatPromptTemplate.form_template("write me an essay about {topic} with 100 words")

add_routes(
    app,
    prompt1|model,
    path="/essay"
)

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(App,host="localhost",port=8000)
