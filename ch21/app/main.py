# FastAPI, Cookie aur Body import karo
from fastapi import FastAPI, Cookie, Body
from typing import Annotated
from pydantic import BaseModel, Field

# FastAPI app banao
app = FastAPI()

# Pydantic model se cookies handle karna
# ## Cookies with a Pydantic Model
# class ProductCookies(BaseModel):
#   session_id: str
#   preferred_category: str | None = None
#   tracking_id: str | None = None

# @app.get("/products/recommendations")
# async def get_recommendations(cookies: Annotated[ProductCookies, Cookie()]):
#   response = {"session_id": cookies.session_id}
#   if cookies.preferred_category:
#     response["message"] = f"Recommendations for {cookies.preferred_category} products"
#   else:
#     response["message"] = f"Default recommendations for session {cookies.session_id}"
#   if cookies.tracking_id:
#       response["tracking_id"] = cookies.tracking_id
#   return response

# curl -H "Cookie: session_id=abc123; preferred_category=Electronics; tracking_id=xyz789" http://127.0.0.1:8000/products/recommendations

## Forbidding Extra Cookies - sirf defined cookies hi allow
# class ProductCookies(BaseModel):
#   model_config = {"extra": "forbid"}
#   session_id: str
#   preferred_category: str | None = None
#   tracking_id: str | None = None

# @app.get("/products/recommendations")
# async def get_recommendations(cookies: Annotated[ProductCookies, Cookie()]):
#   response = {"session_id": cookies.session_id}
#   if cookies.preferred_category:
#     response["message"] = f"Recommendations for {cookies.preferred_category} products"
#   else:
#     response["message"] = f"Default recommendations for session {cookies.session_id}"
#   if cookies.tracking_id:
#       response["tracking_id"] = cookies.tracking_id
#   return response

# Combining Cookie with Body Parameters - cookies aur body dono ka use
class ProductCookies(BaseModel):
  model_config = {"extra": "forbid"}  # Extra cookies allow nahi
  session_id: str = Field(title="Session ID", description="User session identifier")
  preferred_category: str | None = Field(default=None, title="Preferred Category", description="User's preferred product category")

# Price filter ke liye body parameter
class PriceFilter(BaseModel):
    min_price: float = Field(ge=0, title="Minimum Price", description="Minimum price for recommendations")
    max_price: float | None = Field(default=None, title="Maximum Price", description="Maximum price for recommendations")

# POST endpoint - cookie aur body dono se data le raha hai
@app.post("/products/recommendations")
async def get_recommendations(
   cookies: Annotated[ProductCookies, Cookie()],  # Cookies se data
   price_filter: Annotated[PriceFilter, Body(embed=True)]  # Body se data
   ):
  # Response banao
  response = {"session_id": cookies.session_id}
  if cookies.preferred_category:
    response["category"] = cookies.preferred_category
  # Price range add karo
  response["price_range"] = {
        "min_price": price_filter.min_price,
        "max_price": price_filter.max_price
    }
  # Final message return karo
  response["message"] = f"Recommendations for session {cookies.session_id} with price range {price_filter.min_price} to {price_filter.max_price or 'unlimited'}"
  return response

# Curl command - cookie aur body dono ke saath request
# curl -X POST -H "Cookie: session_id=abc123; preferred_category=Electronics" -H "Content-Type: application/json" -d "{\"price_filter\":{\"min_price\":50.0,\"max_price\":1000.0}}" http://127.0.0.1:8000/products/recommendations