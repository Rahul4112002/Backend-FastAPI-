# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                    SCHEMAS.PY - DATA VALIDATION                              ║
# ║                    (Pydantic Models for API)                                 ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

# 🔍 YE FILE KYA HAI?
# ===================
# schemas.py mein PYDANTIC MODELS define karte hain
# Ye API request/response ko VALIDATE karte hain
#
# 🎯 PURPOSE (Maksad):
# 1. API input validation (Request body)
# 2. API output formatting (Response)
# 3. Data type checking
# 4. Automatic documentation
# 5. Type hints provide karna
#
# 📂 FILE LOCATION:
# ch3/app/user/schemas.py
#
# 🔄 MODEL vs SCHEMA:
# Model (models.py)  → Database table (SQLAlchemy)
# Schema (schemas.py) → API validation (Pydantic)


# ┌─────────────────────────────────────────────────────────────────────────────┐
# │  TYPICAL SCHEMAS (Future mein aise honge)                                   │
# └─────────────────────────────────────────────────────────────────────────────┘

# ============== IMPORTS ==============
# from pydantic import BaseModel, EmailStr, Field
# from typing import Optional


# ============== BASE SCHEMA ==============
# 🔍 Common fields jo saare schemas mein hain
# class UserBase(BaseModel):
#     """
#     Base schema with common fields
#     Other schemas isko inherit karenge
#     """
#     name: str = Field(..., min_length=1, max_length=100)
#     email: EmailStr  # Automatic email validation


# ============== CREATE SCHEMA ==============
# 🔍 Naya user create karte waqt ye use hoga
# Request body validation ke liye
#
# class UserCreate(UserBase):
#     """
#     Schema for creating new user
#     POST /users endpoint mein use hoga
#     """
#     password: str = Field(..., min_length=6)
#     
#     # Example usage in route:
#     # @app.post("/users")
#     # def create_user(user: UserCreate):
#     #     ...


# ============== UPDATE SCHEMA ==============
# 🔍 User update karte waqt (sab fields optional)
#
# class UserUpdate(BaseModel):
#     """
#     Schema for updating user
#     PUT/PATCH /users/{id} mein use hoga
#     Saare fields optional (user kuch bhi update kar sakta hai)
#     """
#     name: Optional[str] = None
#     email: Optional[EmailStr] = None
#     password: Optional[str] = None
#     is_active: Optional[bool] = None


# ============== RESPONSE SCHEMA ==============
# 🔍 API response mein kya data bhejenge
#
# class UserResponse(UserBase):
#     """
#     Schema for API response
#     Password ko exclude karta hai (security!)
#     """
#     id: int
#     is_active: bool
#     
#     class Config:
#         # ORM mode: SQLAlchemy model se Pydantic mein convert
#         orm_mode = True
#     
#     # Example usage:
#     # @app.get("/users/{id}", response_model=UserResponse)
#     # def get_user(id: int):
#     #     ...


# ============== LOGIN SCHEMA ==============
# 🔍 Login ke liye separate schema
#
# class UserLogin(BaseModel):
#     """
#     Schema for user login
#     Sirf email aur password chahiye
#     """
#     email: EmailStr
#     password: str


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                         KEY CONCEPTS                                         ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

# 1. PYDANTIC:
#    - Data validation library
#    - Type checking automatic
#    - Better error messages
#    - FastAPI mein built-in support
#
# 2. DIFFERENT SCHEMAS WHY?:
#    - CREATE: User banate waqt password required
#    - UPDATE: Sab optional (partial update)
#    - RESPONSE: Password nahi bhejte (security)
#    - Different use cases = Different schemas
#
# 3. FIELD VALIDATORS:
#    - min_length: Minimum characters
#    - max_length: Maximum characters
#    - ge (>=), le (<=): Number validation
#    - regex: Pattern matching
#    - EmailStr: Automatic email validation
#
# 4. ORM_MODE:
#    - SQLAlchemy model → Pydantic schema convert
#    - Database object ko direct return kar sakte hain
#    - FastAPI automatic conversion karega


# 💡 WHY SEPARATE SCHEMAS FILE?
# ✅ API contract clearly defined
# ✅ Input validation automatic
# ✅ Documentation auto-generated
# ✅ Type safety
# ✅ Security (password hide karna, etc.)


# 🎯 COMMON PATTERNS:
#
# PATTERN 1: Inheritance
# Base schema → Common fields
# Create/Update → Specific fields add
#
# PATTERN 2: Response excludes sensitive data
# Password database mein store hoga
# But API response mein nahi bhejenge
#
# PATTERN 3: Optional for updates
# Update mein user sirf kuch fields update kar sakta hai
# Isliye Optional[type] use karte hain


# 🔧 EXAMPLE USAGE (Routes mein):
# from app.user.schemas import UserCreate, UserResponse
#
# @app.post("/users", response_model=UserResponse)
# def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     # user.name, user.email, user.password access
#     # Automatic validation by Pydantic!
#     ...


# 📊 SCHEMA TYPES SUMMARY:
# UserBase     → Common fields (inheritance)
# UserCreate   → Creating user (POST)
# UserUpdate   → Updating user (PUT/PATCH)
# UserResponse → API response (GET)
# UserLogin    → Authentication (POST /login)
