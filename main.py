
# Step 1: Import FastAPI
from fastapi import FastAPI, Request

# Step 2: Create FastAPI app instance
app = FastAPI()

# Step 3: Define a GET route
@app.get("/")
def read_root():
    return {"message": "Welcome to My API"}

# Step 4: Define a GET route with query param
@app.get("/greet")
def greet_user(name: str):
    return {"greeting": f"Hello, {name}!"}

# Step 5: Define a POST route that accepts JSON
@app.post("/submit")
async def submit_data(request: Request):
    data = await request.json()   # read incoming JSON
    return {"received": data}
