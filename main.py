from fastapi import FastAPI, HTTPException
import json
import os

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to My API"}


@app.get("/data/{filename}")
def get_any_json(filename: str):
    file_path = f"bank_emp.json"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

