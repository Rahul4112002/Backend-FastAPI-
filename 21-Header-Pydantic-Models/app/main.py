# FastAPI, Header aur Body import karo
from typing import Annotated
from fastapi import FastAPI, Header, Body
from pydantic import BaseModel, Field

# FastAPI app banao
app = FastAPI()

## Headers with a Pydantic Model - Pydantic se headers handle karna

# Header fields define karo
class ProductHeaders(BaseModel):
  authorization: str  # Required - authentication ke liye
  accept_language: str | None = None  # Optional - language preference
  x_tracking_id: list[str] = []  # Multiple tracking IDs - list me store

# GET endpoint - headers ko read karke return karo
@app.get("/products")
async def get_product(headers: Annotated[ProductHeaders, Header()]):
    # Saare headers return karo
    return {
        "headers": headers
    }

# Curl command - multiple headers ke saath request
# curl -H "Authorization: Bearer token123" -H "Accept-Language: en-US" -H "X-Tracking-Id: track1" -H "X-Tracking-Id: track2" http://127.0.0.1:8000/products

# Forbidding Extra Headers - sirf defined headers hi allow karo
# class ProductHeaders(BaseModel):
#   model_config = {"extra":"forbid"}
#   authorization: str
#   accept_language: str | None = None
#   x_tracking_id: list[str] = []

# @app.get("/products")
# async def get_product(headers: Annotated[ProductHeaders, Header()]):
#     return {
#         "headers": headers
#     }

# Curl command - extra header bhejne par error aayega (extra="forbid" ki wajah se)
# curl -H "Authorization: Bearer token123" -H "Accept-Language: en-US" -H "X-Tracking-Id: track1" -H "X-Tracking-Id: track2" -H "extra-header: h123" http://127.0.0.1:8000/products