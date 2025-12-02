# CH16 - Multiple Body Parameters
# Purpose: Ek request mein multiple Pydantic models use karna

from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Annotated
app = FastAPI()

# ============ DEFINE MODELS ============
# Product model
class Product(BaseModel):
  name: str
  price:float
  stock: int | None = None

# Seller model
class Seller(BaseModel):
  username: str
  full_name: str | None = None

# ============ MULTIPLE BODY PARAMETERS ============
# Dono models ko request body mein bhejo
# @app.post("/product")
# async def create_product(product: Product, seller:Seller):
#   return {"product": product, "seller":seller}

# ============ OPTIONAL BODY PARAMETER ============
# seller optional hai (None ho sakta hai)
# @app.post("/product")
# async def create_product(product: Product, seller:Seller | None = None):
#   return {"product": product, "seller":seller}

# ============ SINGULAR VALUE IN BODY ============
# Body() use karke simple values ko bhi body mein include karo
# @app.post("/product")
# async def create_product(
#   product: Product, 
#   seller:Seller, 
#   sec_key: Annotated[str, Body()]  # String ko body parameter banaya
#   ):
#   return {"product": product, "seller":seller, "sec_key":sec_key}

# ============ WITHOUT EMBED ============
# Direct object format
# Request: {"name": "Product", "price": 100, "stock": 10}
# @app.post("/product")
# async def create_product(product: Product):
#   return product

# ============ WITH EMBED ============
# embed=True - object ko nested format mein bhejo
# Request: {"product": {"name": "Product", "price": 100, "stock": 10}}
# @app.post("/product")
# async def create_product(product: Annotated[Product, Body(embed=True)]):
#   return product

# embed=True use cases:
# ✅ Single model ko bhi nested format mein chahiye
# ✅ Consistency - multiple models ke saath same structure
# ✅ Frontend ko clear structure