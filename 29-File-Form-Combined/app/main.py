# FastAPI, File upload aur Form import karo
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from typing import Annotated
import os  # File operations ke liye
import shutil  # File copy karne ke liye

# FastAPI app banao
app = FastAPI()

# HTML form - username aur file dono accept karta hai
@app.get("/", response_class=HTMLResponse)
async def get_form():
    return """
    <html>
        <head>
            <title>User Profile Upload</title>
        </head>
        <body>
            <h2>User Profile Form</h2>
            <form action="/user-with-file/" enctype="multipart/form-data" method="post">
                <label for="username">Username:</label><br>
                <input type="text" id="username" name="username" required><br><br>
                <label for="file">Profile Picture (optional):</label><br>
                <input type="file" id="file" name="file" accept="image/*"><br><br>
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
    """

# Form data + File upload - dono ek saath handle karo
@app.post("/user-with-file/")
async def create_user_with_file(
    username: Annotated[str, Form()],  # Form se username
    file: Annotated[UploadFile | None, File()] = None  # Optional file upload
):
    response = {"username": username}  # Response mein username add karo
    
    # Agar file upload hui hai toh use save karo
    if file:
        save_path = f"uploads/{file.filename}"
        os.makedirs("uploads", exist_ok=True)  # uploads folder banao
        # File ko save karo
        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        response["filename"] = file.filename  # Response mein filename add karo
    
    return response



