# ==================== IMPORTS (Libraries ko import karna) ====================
# FastAPI library se FastAPI class ko import kar rahe hain
# Ye class humein web API banane mein madad karti hai
from fastapi import FastAPI

# ==================== APP INSTANCE (Application ka object banana) ====================
# FastAPI() se ek application instance bana rahe hain
# Ye 'app' variable humara main application hai jisme saare routes define honge
# Isko hum FastAPI ka "heart" bhi keh sakte hain
app = FastAPI()

# ==================== ROUTE DEFINITION (API Endpoint banana) ====================
# @app.get("/") - Ye ek decorator hai jo batata hai ki ye function GET request handle karega
# "/" - Ye root URL hai (jaise: http://localhost:8000/)
# Matlab jab koi browser mein "/" par jayega, ye function chalega
@app.get("/")
def home():
  # Ye function automatically JSON response return karega
  # Dictionary ko FastAPI automatically JSON format mein convert kar deta hai
  # Output: {"message": "Hello Fast API"}
  return {"message": "Hello Fast API"}

# ==================== INSTALLATION (Kaise Install Karein?) ====================
# Terminal mein ye command run karein:
# pip install "fastapi[standard]"
# random commit

# Explanation:
# - pip: Python package installer
# - install: Install karne ka command
# - "fastapi[standard]": FastAPI with all standard dependencies
# - [standard]: Isme uvicorn, jinja2 aur saari zaroori cheezein aa jati hain
# - Quotes ("") zaroori hain! Bina quotes ke error aa sakta hai
#
# ==================== KAISE CHALAYE? (Modern Way - Recommended) ====================
# Terminal mein ye command run karein:
# fastapi dev main.py
# 
# Explanation:
# - fastapi: FastAPI ka built-in CLI tool
# - dev: Development mode (auto-reload enabled)
# - main.py: Ye file ka naam
# - Automatically port 8000 par run hoga
# - Code change hone par auto-restart ho jayega
#
# ==================== PURANA TARIKA (Alternative - Old Way) ====================
# Agar tumhare mentor ne purana tarika sikhaya to ye bhi kaam karega:
# uvicorn main:app --reload
# 
# Dono tarike sahi hain, but "fastapi dev" latest aur easy hai!
#
# ==================== BROWSER MEIN KAISE DEKHE? ====================
# Browser mein jao: http://localhost:8000/
# Output dikhega: {"message": "Hello Fast API"}
#
# Interactive Docs: http://localhost:8000/docs
# Alternative Docs: http://localhost:8000/redoc