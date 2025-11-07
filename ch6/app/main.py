# CH6 - Path Parameters with Type Hints
# Purpose: URL path parameters mein data types ka use seekhna

from fastapi import FastAPI

app = FastAPI()

## Bina type ke parameter (kuch bhi accept karega - not recommended)
@app.get("/product/{product_id}")
async def single_product(product_id):
    return {"response":"Single Data Fetched", "product_id": product_id}

# Commented Examples:

# Integer type parameter - sirf numbers accept karega
# @app.get("/product/{product_id}")
# async def single_product(product_id:int):
#     return {"response":"Single Data Fetched", "product_id": product_id}

# String type parameter - text accept karega
# @app.get("/product/{product_title}")
# async def single_product(product_title:str):
#     return {"response":"Single Data Fetched", "product_title": product_title}