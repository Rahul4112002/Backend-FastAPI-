# FastAPI aur File upload utilities import karo
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import Annotated
import os  # File operations ke liye
import shutil  # File copy karne ke liye

# FastAPI app banao
app = FastAPI()


# HTML form for testing - multiple files upload page
@app.get("/", response_class=HTMLResponse)
async def main():
    return """
    <html>
        <body>
            <h2>Multiple Files Upload (UploadFile)</h2>
            <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
                <input name="files" type="file" multiple>
                <input type="submit" value="Upload">
            </form>
        </body>
    </html>
    """

# Multiple files upload endpoint - ek saath kai files upload karo
@app.post("/uploadfiles/")
async def create_upload_file(files: Annotated[list[UploadFile], File()]):
    save_files = []  # Uploaded files ki list
    os.makedirs("uploads", exist_ok=True)  # uploads folder banao
    
    # Har file ko loop mein process karo
    for file in files:
        save_path = f"uploads/{file.filename}"
        # File content ko save karo
        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        # Saved file ka naam list mein add karo
        save_files.append({"filename": file.filename})
    
    # Saari uploaded files ki list return karo
    return save_files