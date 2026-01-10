# FastAPI aur Pydantic import karo
from fastapi import FastAPI
from pydantic import BaseModel, Field

# FastAPI app banao
app = FastAPI()

# Field-level Examples ka use karke - har field me alag example
# ## Using Field-level Examples
class Product(BaseModel):
    name: str = Field(examples=["Moto E"])
    price: float = Field(examples=[23.56])
    stock: int | None = Field(default=None, examples=[43])

# @app.post("/products")
# async def create_product(product: Product):
#     return product

## Using Pydantic's json_schema_extra - poore model ka ek example
# class Product(BaseModel):
#   name: str
#   price: float
#   stock: int | None = None

#   # Model config me complete example define karo
#   model_config = {
#     "json_schema_extra": {
#       "examples": [
#         {
#           "name": "Moto E",
#           "price": 34.56,
#           "stock": 45
#         }
#       ]
#     }
#   }

# POST endpoint - product create karne ke liye
@app.post("/products")
async def create_product(product: Product):
    # Product ko return karo
    return product