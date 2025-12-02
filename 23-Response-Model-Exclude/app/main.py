# FastAPI aur Pydantic import karo
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Any

# FastAPI app banao
app = FastAPI()

# Product ka complete model
class Product(BaseModel):
  id: int
  name: str
  price : float
  stock: int | None = None

# ProductOut - sirf kuch fields ke liye
class ProductOut(BaseModel):
  name: str
  price : float

## response_model Parameter - decorator me response model define karo
# Bina response_model ke - validation nahi hogi
# @app.get("/products/")
# async def get_products():
#   return {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5}

# response_model ke saath - response validate hoga aur document me aayega
@app.get("/products/", response_model=Product)
async def get_products():
  # Product type ka data return karo
  return {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5}


# List of products return karna - response_model me List[Product] use karo
# @app.get("/products/", response_model=List[Product])
# async def get_products():
#   return [
#        {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5},
#        {"id": 2, "name": "Redmi 4", "price": 55.33, "stock": 7}
#     ]

# Extra fields automatic filter ho jayenge - sirf Product model ke fields rahenge
# @app.get("/products/", response_model=List[Product])
# async def get_products():
#   return [
#        {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5, "description": "Hello Desc1"},
#        {"id": 2, "name": "Redmi 4", "price": 55.33, "stock": 7, "description": "Hello Desc2"}
#     ]

# POST endpoint - input aur output dono Product type
# @app.post("/products/", response_model=Product)
# async def create_product(product: Product):
#   return product

# User example - sensitive data filter karna
# BaseUser model - bina password ke
# class BaseUser(BaseModel):
#     username: str
#     full_name: str | None = None

# UserIn - password ke saath (input ke liye)
# class UserIn(BaseUser):
#     password: str

# Password input me lenge lekin response me nahi aayega (response_model=BaseUser)
# @app.post("/users/", response_model=BaseUser)
# async def create_user(user: UserIn):
#   return user

# response_model aur return type dono ka use - best practice
# @app.post("/products/", response_model=Product)
# async def create_product(product: Product) -> Any:
#   return product

# response_model=None - koi validation nahi, jo return karo wahi response me jayega
# @app.post("/products/", response_model=None)
# async def create_product(product: Product) -> Any:
#   return product