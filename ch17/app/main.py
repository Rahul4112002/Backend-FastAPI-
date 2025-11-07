# FastAPI aur Pydantic ke modules import karo
from fastapi import FastAPI
from pydantic import BaseModel, Field

# FastAPI app banao
app = FastAPI()

## Pydantic's Field - validation ke liye
class Product(BaseModel):
  # Product ka naam - min 3, max 100 characters, sirf letters aur numbers
  name: str = Field(
    title="Product Name",
    description="The name of the product",
    max_length=100,
    min_length=3,
    pattern="^[A-Za-z0-9 ]+$"
  )
  
  # Price - zero se zyada hona chahiye
  price: float = Field(
    gt=0,  # gt = greater than
    title="Product Price",
    description="The price of the product in USD, must be greater than zero"
  )
  
  # Stock - optional field, agar hai toh 0 ya usse zyada
  stock: int | None = Field(
    default=None,  # default value None hai
    ge=0,  # ge = greater than or equal to
    title="Stock Quantity",
    description="The number of items in stock, must be non-negative"
  )

# POST endpoint - product create karne ke liye
@app.post("/product")
async def create_product(product: Product):
  # Product ko wapas return karo
  return product