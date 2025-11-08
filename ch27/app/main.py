from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from typing import Annotated

# FastAPI app banao
app = FastAPI()

# Form data types: application/x-www-form-urlencoded or multipart/form-data

# Simple HTML form for testing (GET -> form page)
@app.get("/", response_class=HTMLResponse)
async def get_form():
    # Chhota sa HTML form jo username/password bhejta hai POST /login/ par
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


@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    # Form se aaya username return karo, aur password ka length (safety ke liye)
    return {"username": username, "password_length": len(password)}


# Example with validation (commented): Form() me min_length/max_length add kar sakte ho
# @app.post("/login/")
# async def login(
#     username: Annotated[str, Form(min_length=3)], 
#     password: Annotated[str, Form(min_length=3, max_length=20)]
#     ):
#     return {"username": username, "password_length": len(password)}