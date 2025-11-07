# CH5 - HTTP Methods & CRUD Operations
# Purpose: Saare HTTP methods (GET, POST, PUT, PATCH, DELETE) seekhna

from fastapi import FastAPI

app = FastAPI()

# ============ GET REQUEST ============
# Data fetch/read karne ke liye

## Sabhi products fetch karo
@app.get("/product")
async def all_products():
  return {"response": "All Products"}

## Single product fetch karo (ID se)
# product_id:int - URL se integer value lega
@app.get("/product/{product_id}")
async def single_product(product_id:int):
  return {"response":"Single Data Fetched", "product_id": product_id}

# ============ POST REQUEST ============
# Naya data create/insert karne ke liye

## Naya product create karo
# new_product: dict - Request body se dictionary accept karega
@app.post("/product")
async def create_product(new_product: dict):
  return {"response": "Product Created", "new product": new_product}

# ============ PUT REQUEST ============
# Complete data update karne ke liye (saari fields bhejni padti hain)

## Product ko completely update karo
@app.put("/product/{product_id}")
async def update_product(new_updated_product: dict, product_id: int):
  return {"response":"Complete Data Updated", "product_id": product_id, "new updated product":new_updated_product}

# ============ PATCH REQUEST ============
# Partial data update karne ke liye (sirf kuch fields update karo)

## Product ko partially update karo
@app.patch("/product/{product_id}")
async def partial_product(new_updated_product: dict, product_id: int):
  return {"response":"Partial Data Updated", "product_id": product_id, "new updated product":new_updated_product}

# ============ DELETE REQUEST ============
# Data delete karne ke liye

## Product ko delete karo
@app.delete("/product/{product_id}")
def delete_product(product_id: int):
    return {"response":"Data Deleted", "product_id": product_id}