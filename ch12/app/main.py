# CH12 - Status Codes
# Purpose: HTTP status codes ko routes mein define karna

from fastapi import FastAPI, status  # status module import karo

app = FastAPI()

# Sample data
PRODUCTS = [
        {
            "id": 1,
            "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
            "price": 109.95,
            "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday"
        },
        {
            "id": 2,
            "title": "Mens Casual Premium Slim Fit T-Shirts ",
            "price": 22.3,
            "description": "Slim-fitting style, contrast raglan long sleeve, three-button henley placket, light weight & soft fabric for breathable and comfortable wearing. And Solid stitched shirts with round neck made for durability and a great fit for casual fashion wear and diehard baseball fans. The Henley style round neckline includes a three-button placket."
        },
        {
            "id": 3,
            "title": "Mens Cotton Jacket",
            "price": 55.99,
            "description": "great outerwear jackets for Spring/Autumn/Winter, suitable for many occasions, such as working, hiking, camping, mountain/rock climbing, cycling, traveling or other outdoors. Good gift choice for you or your family member. A warm hearted love to Father, husband or son in this thanksgiving or Christmas Day."
        },
    ]

# ============ GET - 200 OK ============
# Success response ke liye
@app.get("/product", status_code=status.HTTP_200_OK)
async def all_products():
  return PRODUCTS

@app.get("/product/{product_id}", status_code=status.HTTP_200_OK)
async def single_products(product_id:int):
  for product in PRODUCTS:
    if product["id"] == product_id:
      return product
  
# ============ POST - 201 CREATED ============
# Naya resource create hone par
@app.post("/product", status_code=status.HTTP_201_CREATED)
async def create_product(new_product: dict):
  PRODUCTS.append(new_product)
  return {"status":"created", "new_product":new_product}

# ============ PUT - 200 OK ============
# Update success hone par
@app.put("/product/{product_id}", status_code=status.HTTP_200_OK)
def update_product(product_id: int, new_updated_product: dict):
  for index, product in enumerate(PRODUCTS):
    if product["id"] == product_id:
      PRODUCTS[index] = new_updated_product
      return {"status": "Updated", "product_id": product_id, "new updated product": new_updated_product}


# ============ PATCH - 200 OK ============
@app.patch("/product/{product_id}", status_code=status.HTTP_200_OK)
def partial_product(product_id: int, new_updated_product: dict):
    for product in PRODUCTS:
        if product["id"] == product_id:
            product.update(new_updated_product)
            return {"status": "Partial updated", "product_id": product_id, "new updated product": product}

# ============ DELETE - 200 OK ============
@app.delete("/product/{product_id}", status_code=status.HTTP_200_OK)
def delete_product(product_id: int):
    for index, product in enumerate(PRODUCTS):
        if product["id"] == product_id:
            PRODUCTS.pop(index)
            return {"status": "Deleted", "product_id": product_id}

# Common Status Codes:
# 200 OK - Success
# 201 Created - New resource created
# 204 No Content - Delete success (no response body)
# 400 Bad Request - Invalid input
# 404 Not Found - Resource not found
# 500 Internal Server Error - Server error