# Import libraries
from app import model
from fastapi import FastAPI
from dto import dto

# Instantiating the model
model = model.Token()

# Determining how queries work
app = FastAPI()

# Health check
@app.get("/health")
def health_check():
    '''health check'''
    return {"code": 200, "status": "OK"}

# Request for predict
@app.post("/predict", response_model = dto.PredictionOut)
async def answer(user_request: dto.UserRequestIn):
    '''function for processing a request and issuing a response'''
    text = user_request.text
    prediction = model.predict(text)
    return {'prediction': prediction}
