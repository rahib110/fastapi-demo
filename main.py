from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to My API"}

@app.get("/data")
def get_json_data():
    with open("bank_emp.json", "r") as file:
        data = json.load(file)
    return data

