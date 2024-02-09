from fastapi import FastAPI
from pydantic import BaseModel
from enigma import enigma_guard
from dotenv import load_dotenv

load_dotenv()

from chat import send_prompt

app = FastAPI()

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

        
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)