# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                 SERVICES.PY - BUSINESS LOGIC LAYER                           ║
# ║                 (Database Operations & Business Rules)                       ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

# 🔍 YE FILE KYA HAI?
# ===================
# services.py mein BUSINESS LOGIC aur DATABASE OPERATIONS hote hain
# Routes yahan se functions call karte hain
#
# 🎯 PURPOSE (Maksad):
# 1. Database CRUD operations (Create, Read, Update, Delete)
# 2. Business logic implement karna
# 3. Data processing
# 4. Password hashing
# 5. Complex queries
# 6. Data validation (business rules)
#
# 📂 FILE LOCATION:
# ch3/app/user/services.py
#
# 🔗 FLOW:
# Route → Service → Database
# Database → Service → Route


# ┌─────────────────────────────────────────────────────────────────────────────┐
# │  TYPICAL STRUCTURE (Future mein aise hoga)                                  │
# └─────────────────────────────────────────────────────────────────────────────┘

# ============== IMPORTS ==============
# from sqlalchemy.orm import Session
# from app.user import models, schemas
# from passlib.context import CryptContext  # Password hashing
# from typing import Optional, List


# ============== PASSWORD HASHING SETUP ==============
# 🔍 Password security ke liye
# Plain text password kabhi store nahi karte!
#
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
#
# def hash_password(password: str) -> str:
#     """Password ko hash karta hai"""
#     return pwd_context.hash(password)
#
# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     """Password verify karta hai"""
#     return pwd_context.verify(plain_password, hashed_password)


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                         CRUD FUNCTIONS                                       ║
# ╚══════════════════════════════════════════════════════════════════════════════╝


# ============== CREATE USER ==============
# def create_user(db: Session, user: schemas.UserCreate) -> models.User:
#     """
#     Naya user database mein create karta hai
#     
#     Steps:
#     1. Check if email already exists
#     2. Hash password
#     3. Create user object
#     4. Save to database
#     5. Return created user
#     """
#     
#     # 🔍 STEP 1: Check duplicate email
#     existing_user = db.query(models.User).filter(
#         models.User.email == user.email
#     ).first()
#     
#     if existing_user:
#         raise ValueError("Email already registered")
#     
#     
#     # 🔍 STEP 2: Hash password (Security!)
#     hashed_password = hash_password(user.password)
#     
#     
#     # 🔍 STEP 3: Create user object
#     db_user = models.User(
#         name=user.name,
#         email=user.email,
#         password=hashed_password  # Hashed password store karo
#     )
#     
#     
#     # 🔍 STEP 4: Save to database
#     db.add(db_user)        # Add to session
#     db.commit()            # Save to database
#     db.refresh(db_user)    # Refresh to get ID and defaults
#     
#     
#     # 🔍 STEP 5: Return created user
#     return db_user


# ============== GET ALL USERS ==============
# def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[models.User]:
#     """
#     Saare users fetch karta hai with pagination
#     
#     Args:
#         skip: Kitne records skip karein (offset)
#         limit: Kitne records fetch karein
#     
#     Returns:
#         List of user objects
#     """
#     
#     # 🔍 SQLAlchemy query:
#     # - offset(): Skip first N records
#     # - limit(): Get only N records
#     # - all(): Return list
#     
#     return db.query(models.User).offset(skip).limit(limit).all()


# ============== GET USER BY ID ==============
# def get_user_by_id(db: Session, user_id: int) -> Optional[models.User]:
#     """
#     Specific user fetch karta hai by ID
#     
#     Args:
#         user_id: User ka ID
#     
#     Returns:
#         User object ya None (agar nahi mila)
#     """
#     
#     # 🔍 Query by primary key:
#     # - filter(): WHERE condition
#     # - first(): Pehla result (ya None)
#     
#     return db.query(models.User).filter(models.User.id == user_id).first()


# ============== GET USER BY EMAIL ==============
# def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
#     """
#     Email se user find karta hai (Login ke liye useful)
#     """
#     
#     return db.query(models.User).filter(models.User.email == email).first()


# ============== UPDATE USER ==============
# def update_user(
#     db: Session,
#     user_id: int,
#     user_update: schemas.UserUpdate
# ) -> Optional[models.User]:
#     """
#     User ko update karta hai
#     
#     Steps:
#     1. Find user
#     2. Update fields (jo provide kiye gaye)
#     3. Save to database
#     4. Return updated user
#     """
#     
#     # 🔍 STEP 1: Find user
#     db_user = get_user_by_id(db, user_id)
#     
#     if not db_user:
#         return None  # User not found
#     
#     
#     # 🔍 STEP 2: Update fields (only provided ones)
#     update_data = user_update.dict(exclude_unset=True)
#     # exclude_unset=True: Only update jo fields provide kiye
#     
#     # Password ko hash karna hai?
#     if "password" in update_data:
#         update_data["password"] = hash_password(update_data["password"])
#     
#     # Update attributes
#     for field, value in update_data.items():
#         setattr(db_user, field, value)
#     
#     
#     # 🔍 STEP 3: Save
#     db.commit()
#     db.refresh(db_user)
#     
#     
#     # 🔍 STEP 4: Return
#     return db_user


# ============== DELETE USER ==============
# def delete_user(db: Session, user_id: int) -> bool:
#     """
#     User ko delete karta hai
#     
#     Returns:
#         True if deleted, False if not found
#     """
#     
#     # 🔍 Find user
#     db_user = get_user_by_id(db, user_id)
#     
#     if not db_user:
#         return False  # Not found
#     
#     
#     # 🔍 Delete
#     db.delete(db_user)
#     db.commit()
#     
#     return True  # Success


# ============== AUTHENTICATE USER (Login) ==============
# def authenticate_user(db: Session, email: str, password: str) -> Optional[models.User]:
#     """
#     User authentication (Login)
#     
#     Steps:
#     1. Find user by email
#     2. Verify password
#     3. Return user if valid
#     """
#     
#     # 🔍 Find user
#     user = get_user_by_email(db, email)
#     
#     if not user:
#         return None  # Email not found
#     
#     
#     # 🔍 Verify password
#     if not verify_password(password, user.password):
#         return None  # Wrong password
#     
#     
#     return user  # Authentication successful


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                         KEY CONCEPTS                                         ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

# 1. SEPARATION OF CONCERNS:
#    - Routes: Request/Response handling
#    - Services: Business logic
#    - Models: Database structure
#    - Clear responsibilities!
#
# 2. DATABASE SESSION:
#    - db parameter har function mein
#    - Route se inject hota hai (Depends)
#    - CRUD operations perform karta hai
#
# 3. RETURN TYPES:
#    - models.User: Database object
#    - Optional[models.User]: Mil sakta hai ya nahi
#    - List[models.User]: Multiple users
#    - bool: Success/Failure
#
# 4. QUERY PATTERNS:
#    - db.query(Model): Query start
#    - .filter(): WHERE clause
#    - .first(): Single result
#    - .all(): Multiple results
#    - .offset().limit(): Pagination
#
# 5. CRUD OPERATIONS:
#    - CREATE: db.add() + db.commit()
#    - READ: db.query().filter()
#    - UPDATE: setattr() + db.commit()
#    - DELETE: db.delete() + db.commit()


# 💡 WHY SEPARATE SERVICES FILE?
# ✅ Business logic centralized
# ✅ Routes lightweight rahti hain
# ✅ Reusable functions
# ✅ Easy to test
# ✅ Database logic ek jagah
# ✅ Multiple routes same service use kar sakte hain


# 🎯 BEST PRACTICES:
#
# PRACTICE 1: One function = One responsibility
# create_user sirf user create kare
# get_users sirf users fetch kare
#
# PRACTICE 2: Error handling
# None return karo agar not found
# Raise exception for business rule violations
#
# PRACTICE 3: Type hints
# Proper type hints documentation ka kaam karte hain
#
# PRACTICE 4: Password security
# KABHI plain text password store mat karo!
# Hamesha hash use karo


# 🔒 SECURITY TIPS:
# ✅ Password hashing (bcrypt)
# ✅ SQL injection prevention (ORM use karo)
# ✅ Sensitive data filter karo (response_model use)
# ✅ Input validation (Pydantic schemas)


# 📊 SERVICES SUMMARY:
# Function          | Purpose
# ----------------- | -----------------
# create_user       | New user create
# get_users         | List all users
# get_user_by_id    | Find by ID
# get_user_by_email | Find by email (login)
# update_user       | Update user
# delete_user       | Delete user
# authenticate_user | Login validation
