# CH14 - Path Parameter Validation
# Purpose: Path parameters ko validate karna (Path & Query use karke)

from fastapi import FastAPI, Path, Query
from typing import Annotated
app = FastAPI()

PRODUCTS = [
    {"id": 1, "title": "Ravan Backpack", "price": 109.95, "description": "Perfect for everyday use and forest walks."},
    {"id": 2, "title": "Slim Fit T-Shirts", "price": 22.3, "description": "Comfortable, slim-fitting casual shirts."},
    {"id": 3, "title": "Cotton Jacket", "price": 55.99, "description": "Great for outdoor activities and gifting."},
]

# ============ BASIC PATH PARAMETER ============
# Bina validation ke simple path parameter
@app.get("/products/{product_id}") 
async def get_product(product_id: int): 
    for product in PRODUCTS: 
        if product["id"] == product_id: 
            return product 
        return {"error": "Product not found"}

# ============ NUMERIC VALIDATION ============
# ge=1 - greater than or equal to 1
# le=3 - less than or equal to 3
# product_id sirf 1, 2, 3 ho sakta hai
# @app.get("/products/{product_id}") 
# async def get_product(product_id: Annotated[int, Path(ge=1, le=3)]): 
#     for product in PRODUCTS: 
#         if product["id"] == product_id: 
#             return product 
#     return {"error": "Product not found"}

# ============ METADATA WITH PATH ============
# title & description documentation ke liye
# @app.get("/products/{product_id}")
# async def get_product(product_id: Annotated[int, Path(title="The ID of the product", description="This is product id")]):
#     for product in PRODUCTS:
#         if product["id"] == product_id:
#             return product
#     return {"error": "Product not found"}

# ============ COMBINING PATH & QUERY PARAMETERS ============
# gt=0 - greater than 0
# le=100 - less than or equal to 100
# search - optional query parameter with max_length=20
# @app.get("/products/{product_id}")
# async def get_product(
#     product_id: Annotated[int, Path(gt=0, le=100)],
#     search: Annotated[str | None, Query(max_length=20)] = None
# ):
#     for product in PRODUCTS:
#         if product["id"] == product_id:
#             if search and search.lower() not in product["title"].lower():
#                 return {"error": "Product does not match search term"}
#             return product
#     return {"error": "Product not found"}

# Validation Options:
# gt - greater than
# ge - greater than or equal to
# lt - less than
# le - less than or equal to
# min_length - minimum string length
# max_length - maximum string length