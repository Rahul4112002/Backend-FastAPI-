# FastAPI aur Pydantic import karo
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Any, Optional

# FastAPI app banao
app = FastAPI()

## Excluding Unset Default Values - jo fields set nahi hai unhe response me mat bhejo

# Database - products ka dummy data
products_db = {
    "1": {"id": "1", "name": "Laptop", "price": 999.99, "stock": 10, "is_active": True},
    "2": {"id": "2", "name": "Smartphone", "price": 499.99, "stock": 50, "is_active": False}
}

# Product model - kuch fields optional hai with default values
class Product(BaseModel):
    id: str
    name: str
    price: float
    description: Optional[str] = None  # Optional field
    tax: float = 15.0  # Default value hai

# response_model_exclude_unset=True - jo fields set nahi hai woh response me nahi aayenge
# Yaha description aur tax database me nahi hai, toh response me bhi nahi aayenge
@app.get("/products/{product_id}", response_model=Product, response_model_exclude_unset=True)
async def get_product(product_id: str):
    # Database se product fetch karo
    return products_db.get(product_id, {})

## Including Specific Fields - sirf specific fields hi response me bhejo
# response_model_include - sirf name aur price hi response me aayega
# @app.get("/products/{product_id}", response_model=Product, response_model_include={"name", "price"})
# async def get_product(product_id: str):
#     return products_db.get(product_id, {})

# ## Excluding Specific Fields - kuch fields ko response se remove karo
# response_model_exclude - tax aur description response me nahi aayenge
# @app.get("/products/{product_id}", response_model=Product, response_model_exclude={"tax", "description"})
# async def get_product(product_id: str):
#     return products_db.get(product_id, {})