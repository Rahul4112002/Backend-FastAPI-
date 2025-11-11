from tables import create_tables

# Create Tables
from fastapi import FastAPI
from tables import create_tables

# FastAPI app banao
app = FastAPI()

# App start hote hi database tables create karo
@app.on_event("startup")
def startup():
  create_tables()  # Tables ko database mein banao (users, posts, profile, address relationships ke saath)