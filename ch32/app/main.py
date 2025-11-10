# FastAPI aur HTTPException import karo
from fastapi import FastAPI, HTTPException

# FastAPI app banao
app = FastAPI()

# Dummy data - items dictionary
items = {
  "apple": "A juicy fruit", 
  "banana": "A yellow delight"
  }

## Using HTTPException - error raise karne ke liye
@app.get("/items/{item_id}")
async def read_item(item_id: str):
  # Agar item nahi mila toh 404 error raise karo
  if item_id not in items:
    raise HTTPException(status_code=404, detail="Item not found")
  # Item mil gaya toh return karo
  return items[item_id]

# Adding Custom Header - error response mein custom header add karo
# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#   if item_id not in items:
#     raise HTTPException(
#       status_code=404, 
#       detail="Item not found",
#       headers={"x-error-type": "itemmissing"}  # Custom header
#       )
#   return items[item_id]

