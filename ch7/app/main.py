# CH7 - Route Order Matters
# Purpose: Routes ka order important hai - specific routes ko pehle define karo

from fastapi import FastAPI

app = FastAPI()

## Ye specific route pehle hai (hard-coded path)
# /product/rode_nt_usb exact match karega
@app.get("/product/rode_nt_usb")
async def single_product():
    return {"response":"Single Data Fetched"}

## Ye dynamic route baad mein hai
# Agar pehla route match nahi hua to ye chalega
# {product_title} - koi bhi value accept karega
@app.get("/product/{product_title}")
async def single_product(product_title:str):
    return {"response":"Single Data Fetched", "product_title": product_title}

# Important: Agar dynamic route pehle hota to specific route kabhi nahi chalta!
