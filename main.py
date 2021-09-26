from fastapi import FastAPI
import uvicorn
from transformers import pipeline
from pydantic import BaseModel

class Summary(BaseModel):
    detail: str


summarizer = pipeline('summarization')

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'It is working fine'}


@app.post('/summary')
def summary(text: Summary):
    x = summarizer(text.detail,max_length=130, min_length=30, do_sample=False)
    summary = x[0]
    print(summary)
    return summary



#uvicorn main:app --reload
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
