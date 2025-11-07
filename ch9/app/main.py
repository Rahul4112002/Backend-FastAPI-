# CH9 - Path Converter (File Paths)
# Purpose: URL mein complete file path accept karna (with slashes)

from fastapi import FastAPI

app = FastAPI()

# :path convertor - slashes (/) ko bhi path ka part banata hai
# Example: /files/home/user/docs/file.txt
# file_path = "home/user/docs/file.txt" milega
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"You requested file at path": file_path}

# Bina :path ke sirf pehla part milta (slash ke pehle tak)