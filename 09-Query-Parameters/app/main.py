# CH11 - Query Parameters
# Purpose: URL mein ?key=value format ke parameters use karna

from fastapi import FastAPI

app = FastAPI()

# ============ SINGLE QUERY PARAMETER ============
# URL: /product?category=electronics
# category ka value URL se automatically extract hoga
@app.get("/product")
async def product(category:str):
  return {"status":"OK", "category":category}

# Commented Examples:

# ============ MULTIPLE QUERY PARAMETERS ============
# URL: /product?category=electronics&limit=10
# @app.get("/product")
# async def product(category:str, limit:int):
#   return {"status":"OK", "category":category, "limit":limit}

# ============ DEFAULT VALUE ============
# Agar limit nahi diya to 10 use hoga
# URL: /product?category=electronics (limit automatic 10 hoga)
# @app.get("/product")
# async def product(category:str, limit:int=10):
#   return {"status":"OK", "category":category, "limit":limit}

# ============ OPTIONAL PARAMETER ============
# category optional hai (None ho sakta hai)
# URL: /product?limit=5 (bina category ke bhi chalega)
# @app.get("/product")
# async def product(limit:int, category:str | None = None):
#   return {"status":"OK", "category":category, "limit":limit}

# ============ PATH + QUERY PARAMETERS ============
# Path parameter: year (URL mein /product/2024)
# Query parameter: category (URL mein ?category=electronics)
# Full URL: /product/2024?category=electronics
# @app.get("/product/{year}")
# async def product(year:str, category:str):
#   return {"status":"OK", "year":year, "category":category}