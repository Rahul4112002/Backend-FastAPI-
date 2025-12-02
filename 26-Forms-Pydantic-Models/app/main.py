# FastAPI, Form aur Pydantic import karo
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from typing import Annotated
from pydantic import BaseModel, Field

# FastAPI app banao
app = FastAPI()

# Simple HTML form for testing - login page
@app.get("/", response_class=HTMLResponse)
async def get_form():
    return """
    <html>
        <body>
            <h2>Login Form</h2>
            <form action="/login/" method="post">
                <label for="username">Username:</label><br>
                <input type="text" id="username" name="username"><br>
                <label for="password">Password:</label><br>
                <input type="password" id="password" name="password"><br><br>
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
    """

## Pydantic Models for Forms - Form data ko validate karne ke liye
class FormData(BaseModel):
    username: str  # Username field
    password: str  # Password field

# Pydantic Models with Validation - min/max length add karo
# class FormData(BaseModel):
#     username: str = Field(min_length=3)  # Username kam se kam 3 characters
#     password: str = Field(min_length=3, max_length=20)  # Password 3-20 characters

# Extra fields forbid karo - sirf defined fields hi accept hongi
# class FormData(BaseModel):
#     username: str = Field(min_length=3)
#     password: str = Field(min_length=3, max_length=20)
#     model_config = {"extra": "forbid"}  # Extra fields nahi chahiye

# POST endpoint - Pydantic model se form data receive karo
@app.post("/login/")
async def login(data: Annotated[FormData, Form()]):
    # Form data ko validate karke return karo
    return data
