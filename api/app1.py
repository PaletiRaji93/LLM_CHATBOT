from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes
import uvicorn
import os
from langchain_ollama import OllamaLLM
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env", override=True)

google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    raise ValueError("GOOGLE_API_KEY is missing. Add it to your .env file.")

app = FastAPI(
title="Langchain Server",
version="1.0",
description="A Simple API Server"
)

# Google Gemini model

model = ChatGoogleGenerativeAI(
model="gemini-3.6-flash",
google_api_key=google_api_key
)

# Local Ollama model

llm = OllamaLLM(model="llama3.2")

# Essay prompt

prompt1 = ChatPromptTemplate.from_template(
"Write an essay about {topic} in approximately 100 words."
)

# Poem prompt

prompt2 = ChatPromptTemplate.from_template(
"Write a poem about {topic}."
)

# Google Gemini essay endpoint

add_routes(
app,
prompt1 | model,
path="/essay"
)

# Ollama poem endpoint

add_routes(
app,
prompt2 | llm,
path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
