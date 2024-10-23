from fastapi import FastAPI # instance of fast api
import uvicorn
from model.BankNotes import BankNote
import numpy as np
import pickle
import pandas as pd

app = FastAPI()
pickle_in = open("model/classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.get("/hello")
def read_hello():
    return {"message": "Hello World! I am here! update"}


@app.post("/predict")
def predict_banknote(data:BankNote):
    data = data.dict()
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    if(prediction[0]>0.5):
        prediction="Fake note"
    else:
        prediction="Its a Bank note"
    return {
        'prediction': prediction
    }