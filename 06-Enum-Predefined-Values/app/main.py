# CH8 - Enum (Predefined Values)
# Purpose: Path parameter ko limited/predefined values mein restrict karna

from fastapi import FastAPI
from enum import Enum  # Python ka Enum class
app = FastAPI()

## Predefined categories define karo
# ProductCategory - sirf ye 3 values allowed hain
class ProductCategory(str, Enum):
    books = "books"            # Category 1
    clothing = "clothing"      # Category 2
    electronics = "electronics"  # Category 3

# Endpoint - sirf allowed categories accept karega
# Koi aur value doge to error aayega
@app.get("/product/{category}")
async def get_products(category:ProductCategory):
    return {"response": "Products fetched", "category": category}

# Commented Example - Enum values ko condition mein check karna:
# @app.get("/product/{category}")
# async def get_products(category:ProductCategory):
#     if category == ProductCategory.books:
#         return {"category": category, "message": "Books are awesome!"}
#     elif category.value == "clothing":
#         return {"category": category, "message": "Fashion trends here!"}
#     elif category == ProductCategory.electronics.value:
#         return {"category": category, "message": "Latest gadgets available!"}
#     else:
#         return {"category": category, "message": "Unknown category"}