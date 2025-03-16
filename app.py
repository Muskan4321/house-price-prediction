from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import pandas as pd
import pickle

df = pd.read_csv("BostonHousing.csv")
df.columns = df.columns.str.strip()  

print(df.columns)  

df.columns = df.columns.str.lower()  


with open("house_price.pkl", "rb") as file:
    model = pickle.load(file)

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to the Boston House Price Prediction API!"}

class InputData(BaseModel):
    CRIM: float
    ZN: float
    INDUS: float
    CHAS: float
    NOX: float
    RM: float
    AGE: float
    DIS: float
    RAD: float
    TAX: float
    PTRATIO: float
    B: float
    LSTAT: float

# Prediction endpoint
@app.post("/predict/")
async def predict(data: InputData):
    try:
        features = np.array([[
            data.CRIM, data.ZN, data.INDUS,
            data.CHAS, data.NOX, data.RM,
            data.AGE, data.DIS, data.RAD,
            data.TAX, data.PTRATIO, data.B,
            data.LSTAT
        ]])

        prediction = model.predict(features)
        return {"predicted_price": float(prediction[0])}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
