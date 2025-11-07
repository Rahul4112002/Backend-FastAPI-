# CH4 - Basic FastAPI Application
# Purpose: Simple "Hello World" API banane ka basic structure

# FastAPI ko import karo
from fastapi import FastAPI

# FastAPI instance banao
app = FastAPI()

# Root endpoint (/) - GET request handle karta hai
@app.get("/")
def home():
  # Simple JSON response return karta hai
  return {"message": "Hello Fast API"}