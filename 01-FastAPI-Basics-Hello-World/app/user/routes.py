# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                    ROUTES.PY - API ENDPOINTS                                 ║
# ║                    (User ke saare API routes yahan)                          ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

# 🔍 YE FILE KYA HAI?
# ===================
# routes.py (ya routers.py) mein API ENDPOINTS define karte hain
# Ye client (browser/mobile app) se requests handle karte hain
#
# 🎯 PURPOSE (Maksad):
# 1. API endpoints define karna (URLs)
# 2. HTTP methods handle karna (GET, POST, PUT, DELETE)
# 3. Request data receive karna
# 4. Service layer ko call karna
# 5. Response bhejana
#
# 📂 FILE LOCATION:
# ch3/app/user/routes.py
#
# 🔗 FLOW:
# Client → Route → Service → Database
# Database → Service → Route → Client


# ┌─────────────────────────────────────────────────────────────────────────────┐
# │  TYPICAL STRUCTURE (Future mein aise hoga)                                  │
# └─────────────────────────────────────────────────────────────────────────────┘

# ============== IMPORTS ==============
# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from app.db.config import get_db
# from app.user import schemas, services
# from typing import List


# ============== ROUTER INSTANCE ==============
# 🔍 APIRouter: FastAPI ka router class
# main.py mein is router ko include karenge
#
# router = APIRouter()


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                         CRUD ENDPOINTS                                       ║
# ╚══════════════════════════════════════════════════════════════════════════════╝


# ============== CREATE USER (POST) ==============
# @router.post("/", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
# def create_user(
#     user: schemas.UserCreate,           # Request body (Pydantic validation)
#     db: Session = Depends(get_db)       # Database session (dependency injection)
# ):
#     """
#     Naya user create karo
#     
#     Endpoint: POST /users/
#     Request: {"name": "John", "email": "john@example.com", "password": "secret"}
#     Response: {"id": 1, "name": "John", "email": "john@example.com", "is_active": true}
#     """
#     
#     # 🔍 STEPS:
#     # 1. Check if email already exists
#     # 2. Hash password
#     # 3. Save to database
#     # 4. Return created user
#     
#     return services.create_user(db, user)


# ============== GET ALL USERS (GET) ==============
# @router.get("/", response_model=List[schemas.UserResponse])
# def get_users(
#     skip: int = 0,                      # Pagination: kitne skip karein
#     limit: int = 100,                   # Pagination: kitne fetch karein
#     db: Session = Depends(get_db)
# ):
#     """
#     Saare users ki list get karo
#     
#     Endpoint: GET /users/?skip=0&limit=10
#     Response: [{"id": 1, "name": "John", ...}, {"id": 2, "name": "Jane", ...}]
#     """
#     
#     # 🔍 Query parameters:
#     # skip: Offset for pagination
#     # limit: How many records to fetch
#     
#     return services.get_users(db, skip=skip, limit=limit)


# ============== GET USER BY ID (GET) ==============
# @router.get("/{user_id}", response_model=schemas.UserResponse)
# def get_user(
#     user_id: int,                       # Path parameter (URL se aata hai)
#     db: Session = Depends(get_db)
# ):
#     """
#     Specific user get karo by ID
#     
#     Endpoint: GET /users/1
#     Response: {"id": 1, "name": "John", "email": "john@example.com", ...}
#     """
#     
#     # 🔍 Path parameter:
#     # user_id URL se automatically extract hoga
#     # /users/1 → user_id = 1
#     # /users/42 → user_id = 42
#     
#     user = services.get_user_by_id(db, user_id)
#     
#     if user is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="User not found"
#         )
#     
#     return user


# ============== UPDATE USER (PUT) ==============
# @router.put("/{user_id}", response_model=schemas.UserResponse)
# def update_user(
#     user_id: int,
#     user_update: schemas.UserUpdate,    # Request body
#     db: Session = Depends(get_db)
# ):
#     """
#     User ko update karo
#     
#     Endpoint: PUT /users/1
#     Request: {"name": "John Updated", "email": "newemail@example.com"}
#     Response: Updated user object
#     """
#     
#     updated_user = services.update_user(db, user_id, user_update)
#     
#     if updated_user is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="User not found"
#         )
#     
#     return updated_user


# ============== DELETE USER (DELETE) ==============
# @router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_user(
#     user_id: int,
#     db: Session = Depends(get_db)
# ):
#     """
#     User ko delete karo
#     
#     Endpoint: DELETE /users/1
#     Response: No content (204 status)
#     """
#     
#     success = services.delete_user(db, user_id)
#     
#     if not success:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="User not found"
#         )
#     
#     return None  # 204 No Content


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                         KEY CONCEPTS                                         ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

# 1. APIRouter:
#    - Main app se alag router banata hai
#    - Modular routing ke liye
#    - main.py mein include karna padega
#
# 2. DECORATORS:
#    - @router.get()    → GET request
#    - @router.post()   → POST request
#    - @router.put()    → PUT request (full update)
#    - @router.patch()  → PATCH request (partial update)
#    - @router.delete() → DELETE request
#
# 3. PARAMETERS:
#    - Path parameter: URL mein /{user_id}
#    - Query parameter: URL mein ?skip=0&limit=10
#    - Request body: POST/PUT data
#    - Dependencies: Depends() se inject
#
# 4. RESPONSE_MODEL:
#    - Response ko validate karta hai
#    - Pydantic schema use hota hai
#    - Sensitive data (password) automatically exclude
#
# 5. STATUS_CODE:
#    - 200: OK (success)
#    - 201: Created (new resource)
#    - 204: No Content (deleted)
#    - 404: Not Found
#    - 422: Validation Error


# 💡 WHY SEPARATE ROUTES FILE?
# ✅ API endpoints ek jagah defined
# ✅ Business logic alag (services.py mein)
# ✅ Routes lightweight aur clean
# ✅ Testing easy
# ✅ Multiple developers kaam kar sakte hain


# 🎯 ROUTE PATTERNS:
#
# PATTERN 1: Thin Routes
# - Route sirf request/response handle kare
# - Logic services mein rakho
#
# PATTERN 2: Dependency Injection
# - Depends(get_db) automatic session management
# - Reusable dependencies
#
# PATTERN 3: Error Handling
# - HTTPException use karo
# - Proper status codes
# - Clear error messages


# 🔧 REGISTRATION (main.py mein):
# from app.user.routes import router as user_router
# app.include_router(user_router, prefix="/users", tags=["Users"])
#
# Result:
# POST   /users/          → create_user()
# GET    /users/          → get_users()
# GET    /users/{id}      → get_user()
# PUT    /users/{id}      → update_user()
# DELETE /users/{id}      → delete_user()


# 📊 ROUTES vs SERVICES:
# Routes    → Request/Response handling
# Services  → Business logic, Database operations
# Routes ko thin rakhna chahiye!
