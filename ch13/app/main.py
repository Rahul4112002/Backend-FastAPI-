# CH13 - Advanced Query Parameter Validation
# Purpose: Query parameters ko validate karna (Annotated & Query use karke)

from fastapi import FastAPI, Query  # Query validator import karo
from typing import Annotated  # Type hints ke liye
from pydantic import AfterValidator  # Custom validation ke liye

app = FastAPI()

PRODUCTS = [
    {"id": 1, "title": "Ravan Backpack", "price": 109.95, "description": "Perfect for everyday use and forest walks."},
    {"id": 2, "title": "Slim Fit T-Shirts", "price": 22.3, "description": "Comfortable, slim-fitting casual shirts."},
    {"id": 3, "title": "Cotton Jacket", "price": 55.99, "description": "Great for outdoor activities and gifting."},
]

# ============ BASIC QUERY PARAMETER ============
# Simple search without validation
# @app.get("/products")
# async def get_products(search:str | None = None):
#   if search:
#     search_lower = search.lower()
#     filtered_products = []
#     for product in PRODUCTS:
#       if search_lower in product["title"].lower(): 
#         filtered_products.append(product)
#     return filtered_products
#   return PRODUCTS

# ============ VALIDATION WITHOUT ANNOTATED ============
# max_length=5 - search maximum 5 characters ho sakta hai
# @app.get("/products")
# async def get_products(search:str | None = Query(default=None, max_length=5)):
#   if search:
#     search_lower = search.lower()
#     filtered_products = []
#     for product in PRODUCTS:
#       if search_lower in product["title"].lower(): 
#         filtered_products.append(product)
#     return filtered_products
#   return PRODUCTS

# ============ VALIDATION WITH ANNOTATED ============
# Modern way - type aur validation separate
# @app.get("/products")
# async def get_products(
#   search: 
#     Annotated[
#       str | None,  # Type hint
#       Query(max_length=5)  # Validation
#       ] = None):
#   if search:
#     search_lower = search.lower()
#     filtered_products = []
#     for product in PRODUCTS:
#       if search_lower in product["title"].lower(): 
#         filtered_products.append(product)
#     return filtered_products
#   return PRODUCTS

# Why use Annotated
## Clear separation - type aur validation alag
## Better editor support - tools mein metadata show hota hai
## Python 3.9+ aur FastAPI 0.95+ required
## FastAPI 0.95+ officially recommends (modern approach)

# ============ REQUIRED PARAMETER ============
# min_length=3 - kam se kam 3 characters zaroori
# @app.get("/products/")
# async def get_products(search: Annotated[str, Query(min_length=3)]):
#     if search:
#         search_lower = search.lower()
#         filtered_products = []
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS

# ============ REGEX VALIDATION ============
# pattern="^[a-z]+$" - sirf lowercase letters allowed
# @app.get("/products/")
# async def get_products(search: Annotated[str | None, Query(min_length=3, pattern="^[a-z]+$")] = None):
#     if search:
#         search_lower = search.lower()
#         filtered_products = []
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS

# ============ LIST OF VALUES ============
# Multiple search terms accept karo
# @app.get("/products")
# async def get_products(search: Annotated[list[str] | None, Query()] = None):
#   if search:
#     filtered_products = []
#     for product in PRODUCTS:
#       for s in search:
#         if s.lower() in product["title"].lower():
#           filtered_products.append(product)
#     return filtered_products
#   return PRODUCTS

# ============ ALIAS PARAMETER ============
# URL mein "q" use karo but code mein "search" naam se access
# @app.get("/products/")
# async def get_products(search: Annotated[str | None, Query(alias="q")] = None):
#     if search:
#         search_lower = search.lower()
#         filtered_products = []
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS

# ============ METADATA FOR DOCS ============
# title & description documentation mein dikhega
# @app.get("/products/")
# async def get_products(search: Annotated[
#         str | None,
#         Query(alias="q", title="Search Products", description="Search by product title")
#     ] = None
#     ):
#     if search:
#         search_lower = search.lower()
#         filtered_products = []
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS

# ============ DEPRECATED PARAMETER ============
# deprecated=True - docs mein warning dikhega (purana parameter)
# @app.get("/products/")
# async def get_products(search: Annotated[
#         str | None,
#         Query(deprecated=True)
#     ] = None
#     ):
#     if search:
#         search_lower = search.lower()
#         filtered_products = []
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS

# ============ CUSTOM VALIDATION ============
# def check_valid_id(id: str):
#   if not id.startswith("prod-"):  # Check custom rule
#     raise ValueError("ID must start with 'prod-'")
#   return id

# @app.get("/products/")
# async def get_products(id: Annotated[str | None, AfterValidator(check_valid_id)] = None):
#     if id:
#         return {"id": id, "message": "Valid product ID"}
#     return {"message": "No ID provided"}