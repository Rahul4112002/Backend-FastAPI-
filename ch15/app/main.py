# CH15 - Request Body with Pydantic
# Purpose: Request body ko validate karna using Pydantic models

from fastapi import FastAPI
from pydantic import BaseModel  # Validation ke liye
app = FastAPI()

# ============ WITHOUT PYDANTIC ============
# Simple dict - koi validation nahi
@app.post("/product")
async def create_product(new_product: dict):
  return new_product


# ============ WITH PYDANTIC ============
# Product model - automatic validation
# Define the Product model/schema
class Product(BaseModel):
  id: int  # Integer required
  name: str  # String required
  price: float  # Float required
  stock: int | None = None  # Optional (default None)

# @app.post("/product")
# async def create_product(new_product: Product):
#   return new_product

# ============ ACCESS ATTRIBUTES ============
# Pydantic object ke attributes ko access karo
# @app.post("/product")
# async def create_product(new_product: Product):
#   print(new_product.id)  # Direct attribute access
#   print(new_product.name)
#   print(new_product.price)
#   print(new_product.stock)
#   return new_product

# ============ ADD CALCULATED FIELD ============
# model_dump() - Pydantic model ko dictionary mein convert karo
# @app.post("/product")
# async def create_product(new_product: Product):
#   product_dict = new_product.model_dump()  # Dict mein convert
#   price_with_tax = new_product.price + (new_product.price * 18 / 100)  # 18% tax
#   product_dict.update({"price_with_tax": price_with_tax})  # Naya field add
#   return product_dict

# ============ COMBINING WITH PATH PARAMETER ============
# Path + Body dono ek saath
# @app.put("/products/{product_id}")
# async def update_product(product_id: int, new_updated_product: Product):
#     return {"product_id": product_id, "new_updated_product":new_updated_product}

# ============ ADDING QUERY PARAMETER ============
# Path + Body + Query teenon ek saath
# @app.put("/products/{product_id}")
# async def update_product(product_id: int, new_updated_product: Product, discount: float | None = None):
#     return {"product_id": product_id, "new_updated_product": new_updated_product, "discount": discount}

# Benefits of Pydantic:
# ✅ Automatic type validation
# ✅ Better error messages
# ✅ Auto-generated documentation
# ✅ Type hints for IDE
# ✅ Easy to test