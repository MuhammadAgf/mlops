import requests
from fastapi import FastAPI

app = FastAPI()

from pydantic import BaseModel

import os

MODEL_URL = os.getenv("MODEL_URL", "http://localhost")
#http://localhost:8080/v2/models/content-type-example/infer


class Query(BaseModel):
    text: str

class Response(BaseModel):
    predicted: int

@app.post("/predict")
async def pred(q: Query) -> Response:
    payload = {
        "inputs": [
            {
                "name": "predict_proba",
                "datatype": "BYTES",
                "shape": [1],#len(q.text)],
                "data": [q.text],
           }
        ]
    }
    return Response(predicted=requests.post(f"{MODEL_URL}:8080/v2/models/text-clf/versions/v0.1.0/infer", json=payload).json()['outputs'][0]['data'][0])

@app.get("/")
async def root():
    return {"message": "Hello World"}
