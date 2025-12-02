# CH18 - Nested Models (Submodels)
# Purpose: Ek model ke andar dusra model use karna (nested structure)

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# ============ NESTED MODELS ============
# Submodel - Category model
class Category(BaseModel):
  name : str = Field(
    title="Category Name",
    description="The name of the product category",
    max_length=50,
    min_length=1
  )
  description: str | None = Field(
        default=None,
        title="Category Description",
        description="A brief description of the category",
        max_length=200
    )
  
# Main Model - Product (Category ko use karega)
class Product(BaseModel):
    name: str = Field(
        title="Product Name",
        description="The name of the product",
        max_length=100,
        min_length=1
    )
    price: float = Field(
        gt=0,
        title="Product Price",
        description="The price in USD, must be greater than zero"
    )
    stock: int | None = Field(
        default=None,
        ge=0,
        title="Stock Quantity",
        description="Number of items in stock, must be non-negative"
    )
    category : Category | None = Field(  # Nested model
       default=None,
       title="Product Category",
       description="The category to which the product belongs"
    )

@app.post("/products")
async def create_product(product: Product):
    return product

# Request Example (Nested):
# {
#   "name": "Laptop",
#   "price": 50000,
#   "stock": 10,
#   "category": {
#     "name": "Electronics",
#     "description": "Electronic items"
#   }
# }

# ============ LIST OF SUBMODELS ============
# Commented example - category ab list hai (multiple categories)
# class Product(BaseModel):
#     name: str
#     price: float
#     stock: int | None = None
#     category: list[Category] | None = Field(  # List of categories
#        default=None,
#        title="Product Category"
#     )

# Request Example (List):
# {
#   "name": "Laptop",
#   "price": 50000,
#   "category": [
#     {"name": "Electronics"},
#     {"name": "Computers"}
#   ]
# }