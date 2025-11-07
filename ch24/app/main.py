# FastAPI aur Pydantic import karo
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# FastAPI app banao
app = FastAPI()

# Product ka complete model - input ke liye
class Product(BaseModel):
  id: int
  name: str
  price : float
  stock: int | None = None

# ProductOut - sirf kuch fields return karne ke liye
class ProductOut(BaseModel):
  name: str
  price : float


# Bina return type ke - FastAPI ko nahi pata response kaisa hoga
# # Without Return Type
# @app.get("/products/")
# async def get_products():
#     return [
#        {"status": "OK"},
#        {"status": 200}
#     ]

## Return type annotation - response model specify karo
# -> Product likh kar hum bata rahe hain ki response Product type ka hoga
@app.get("/products/")
async def get_products() -> Product:
    # Single product return karo
    return {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5}

# Required field missing - stock nahi bheja toh error aayega
# @app.get("/products/")
# async def get_products() -> Product:
#     return {"id": 1, "name": "Moto E", "price": 33.44}

# Extra field bhejne par - description ko ignore kar dega (by default)
# @app.get("/products/")
# async def get_products() -> Product:
#     return {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5, "description": "This is moto e"}

# List of products return karna - List[Product] ka use karo
# @app.get("/products/")
# async def get_products() -> List[Product]:
#     return [
#        {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5},
#        {"id": 2, "name": "Redmi 4", "price": 55.33, "stock": 7}
#     ]

# List me extra fields - woh ignore ho jayenge
# @app.get("/products/")
# async def get_products() -> List[Product]:
#     return [
#        {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5, "description": "Hello Desc1"},
#        {"id": 2, "name": "Redmi 4", "price": 55.33, "stock": 7, "description": "Hello Desc2"}
#     ]

# POST endpoint - input aur output dono Product type
# @app.post("/products/")
# async def create_product(product: Product) -> Product:
#   return product

# POST endpoint - input Product hai lekin output ProductOut (sirf kuch fields)
# Sensitive data (jaise id, stock) hide karne ke liye useful
# @app.post("/products/")
# async def create_product(product: Product) -> ProductOut:
#   return product

# User example - password input me hai lekin output me nahi
# BaseUser model - common fields
# class BaseUser(BaseModel):
#     username: str
#     full_name: str | None = None

# UserIn - password ke saath (input ke liye)
# class UserIn(BaseUser):
#     password: str

# POST endpoint - password input me lenge lekin return me nahi bhejenge
# @app.post("/users/")
# async def create_user(user: UserIn) -> BaseUser:
#   return user