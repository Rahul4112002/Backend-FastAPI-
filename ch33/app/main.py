# FastAPI, Request aur JSONResponse import karo
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

# FastAPI app banao
app = FastAPI()

# Dummy data - fruits dictionary
fruits = {
  "apple": "A juicy fruit", 
  "banana": "A yellow delight"
  }

# Create Custom Exception - apna khud ka exception class
class FruitException(Exception):
  def __init__(self, fruit_name: str):
    self.fruit_name = fruit_name

# Custom Exception Handler - FruitException ko handle karne ke liye
@app.exception_handler(FruitException)
async def fruit_exception_handler(request: Request, exc: FruitException):
  # Custom response return karo with status code 418
  return JSONResponse(
    status_code=418,
    content={"message": f"{exc.fruit_name} is not valid"}
  )

# Endpoint - fruit fetch karne ke liye
@app.get("/fruits/{fruit_name}")
async def read_fruit(fruit_name: str):
    # Agar fruit nahi mila toh custom exception raise karo
    if fruit_name not in fruits:
      raise FruitException(fruit_name=fruit_name)
    # Fruit mil gaya toh return karo
    return fruits[fruit_name]