# FastAPI aur Header import karo
from fastapi import FastAPI, Header
from typing import Annotated

# FastAPI app banao
app = FastAPI()

## Header Parameters - request headers se data read karna
@app.get("/products")
async def get_products(user_agent: Annotated[str|None, Header()] = None):
  # User agent header ko return karo
  return user_agent

# Curl command - custom header ke saath request
# curl -H "User-Agent: Mozilla/5.0" http://127.0.0.1:8000/products

## Handling Duplicate Headers - same header multiple times
# Agar ek hi header multiple baar aaye toh list me store hoga
# @app.get("/products")
# async def get_product(x_product_token: Annotated[list[str] | None, Header()] = None):
#     return {
#         "x_product_token": x_product_token or []
#     }

# curl -H "X-Product-Token: token1" -H "X-Product-Token: token2" http://127.0.0.1:8000/products