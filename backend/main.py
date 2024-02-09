from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from backend.tools.enigma import enigma_guard

load_dotenv()

from backend.tools.chat import send_prompt

app = FastAPI()
app.add_middleware(CORSMiddleware,allow_origins=['*'])


@app.get("/")
def read_root():
    return {"Server": "Running"}

@app.post("/api/anonymyze")
def anonymyze(input_text: str):
    anonymyzed_text = enigma_guard.filter(input_text)
    chat_response = send_prompt(anonymyzed_text)
    if "<" and ">" in chat_response:
        deanonymyzed_text = enigma_guard.defilter(chat_response)
        return {"anonymyzed_text": anonymyzed_text, "chat_response": chat_response, "deanonymyzed_text": deanonymyzed_text}
    else:
        return {"anonymyzed_text": anonymyzed_text, "chat_response": chat_response, "deanonymyzed_text": "No Need to deanonymyzed!"}


