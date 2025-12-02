# FastAPI aur exception handling import karo
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

# FastAPI app banao
app = FastAPI()

# Override default validation error handler
# RequestValidationError ko custom tarike se handle karo
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc:RequestValidationError):
  # Plain text response return karo instead of JSON
  return PlainTextResponse(str(exc), status_code=400)

# Endpoint - integer item_id expect karta hai
@app.get("/items/{item_id}")
async def read_item(item_id: int):
  # Agar integer nahi bheja toh custom error message milega
  return item_id

