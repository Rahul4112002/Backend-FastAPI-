# FastAPI, File upload aur utilities import karo
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import Annotated
import os  # File system operations ke liye
import uuid  # Unique filename generate karne ke liye
import shutil  # File copy karne ke liye

# FastAPI app banao
app = FastAPI()


# HTML form for testing - file upload page
@app.get("/", response_class=HTMLResponse)
async def main():
    return """
    <html>
        <body>
            <h2>Single File Upload (bytes)</h2>
            <form action="/files/" enctype="multipart/form-data" method="post">
                <input name="file" type="file">
                <input type="submit" value="Upload">
            </form>
            <h2>Single File Upload (UploadFile)</h2>
            <form action="/uploadfile/" enctype="multipart/form-data" method="post">
                <input name="file" type="file">
                <input type="submit" value="Upload">
            </form>
        </body>
    </html>
    """

# File as bytes - simple file upload (commented example)
# @app.post("/files/")
# async def create_file(file: Annotated[bytes | None, File()] = None):
#     if not file:
#         return {"message": "No file sent"}
#     return {"file size": len(file)}  # File ka size return karo

# File as bytes with save - file ko disk par save karo (commented example)
# @app.post("/files/")
# async def create_file(file: Annotated[bytes | None, File()] = None):
#     if not file:
#         return {"message": "No file sent"}
#     
#     # Unique filename generate karo
#     filename = f"{uuid.uuid4()}.bin"
#     save_path = f"uploads/{filename}"
#
#     # uploads folder banao agar nahi hai
#     os.makedirs("uploads", exist_ok=True)
#
#     # File ko save karo
#     with open(save_path, "wb") as buffer:
#         buffer.write(file)
#
#     return {"file size": len(file)}

# UploadFile - recommended approach for file uploads
@app.post("/uploadfile/")
async def create_upload_file(file: Annotated[UploadFile | None, File()] = None):
    if not file:
        return {"message": "No upload file sent"}
    
    # File ko uploads folder mein save karo
    save_path = f"uploads/{file.filename}"
    os.makedirs("uploads", exist_ok=True)  # Folder banao agar nahi hai
    
    # File content ko copy karo
    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Filename aur content type return karo
    return {"filename": file.filename, "content_type": file.content_type}