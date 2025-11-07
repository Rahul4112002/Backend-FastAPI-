# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                    MODELS.PY - DATABASE MODELS                               ║
# ║                    (Database Table Ki Blueprint)                             ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

# 🔍 YE FILE KYA HAI?
# ===================
# models.py mein DATABASE TABLES ka structure define karte hain
# Ye ORM (Object Relational Mapping) use karta hai
#
# 🎯 PURPOSE (Maksad):
# 1. Database table ka Python class banaa
# 2. Columns define karna (name, email, age, etc.)
# 3. Data types specify karna (String, Integer, Boolean)
# 4. Constraints add karna (unique, nullable, default)
# 5. Relationships define karna (foreign keys)
#
# 📂 FILE LOCATION:
# ch3/app/user/models.py
#
# 💾 DATABASE TABLE:
# Model → Python Class
# Table → Database Table
# Column → Class Attribute
# Row → Class Instance


# ┌─────────────────────────────────────────────────────────────────────────────┐
# │  TYPICAL USER MODEL (Future mein aise hoga)                                 │
# └─────────────────────────────────────────────────────────────────────────────┘

# ============== IMPORTS ==============
# from sqlalchemy import Column, Integer, String, Boolean
# from app.db.config import Base


# ============== USER MODEL CLASS ==============
# class User(Base):
#     """
#     User database model/table
#     Ye class database mein 'users' table banega
#     """
#     
#     # TABLE NAME
#     # Database mein kis naam se table banega
#     __tablename__ = "users"
#     
#     
#     # ========== COLUMNS (Table ke fields) ==========
#     
#     # ID - Primary Key (Unique identifier for each user)
#     # 🔍 primary_key=True: Ye column table ka unique identifier hai
#     # 🔍 index=True: Fast searching ke liye index banata hai
#     id = Column(Integer, primary_key=True, index=True)
#     
#     
#     # NAME - User ka naam
#     # 🔍 String: Text data type
#     # 🔍 index=True: Naam se search karne ke liye fast
#     name = Column(String, index=True)
#     
#     
#     # EMAIL - User ka email (Unique hona chahiye)
#     # 🔍 unique=True: Duplicate emails allowed nahi
#     # 🔍 index=True: Email se login/search ke liye fast
#     email = Column(String, unique=True, index=True)
#     
#     
#     # PASSWORD - Hashed password
#     # 🔍 Plain text password store KABHI nahi karte!
#     # 🔍 Hashing use karte hain (bcrypt, passlib)
#     password = Column(String)
#     
#     
#     # IS_ACTIVE - User active hai ya nahi
#     # 🔍 Boolean: True/False value
#     # 🔍 default=True: Naya user by default active hoga
#     is_active = Column(Boolean, default=True)


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                         KEY CONCEPTS                                         ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

# 1. ORM (Object Relational Mapping):
#    - Python Class ↔ Database Table
#    - Class attribute ↔ Table Column
#    - Class instance ↔ Table Row
#    - SQL queries nahi likhne padte!
#
# 2. COLUMN TYPES (Common ones):
#    - Integer: Numbers (1, 2, 100)
#    - String: Text ("John", "john@email.com")
#    - Boolean: True/False
#    - Float: Decimal numbers (99.99)
#    - DateTime: Date and time
#    - Text: Long text (descriptions)
#
# 3. CONSTRAINTS:
#    - primary_key: Unique identifier
#    - unique: Duplicate values not allowed
#    - nullable: Can be empty (default True)
#    - default: Default value agar provide nahi kiya
#    - index: Fast searching
#
# 4. Base CLASS:
#    - config.py se import hota hai
#    - Saare models Base ko inherit karte hain
#    - SQLAlchemy ko batata hai ye model hai


# 💡 WHY SEPARATE MODELS FILE?
# ✅ Database structure clearly defined
# ✅ Ek jagah saare table columns
# ✅ Easy to modify table structure
# ✅ Migrations easier (Alembic use karke)
# ✅ Type hints aur autocomplete milta hai


# 🔧 EXAMPLE USAGE (Code mein aise use hoga):
# from app.user.models import User
#
# # Naya user create
# new_user = User(
#     name="John Doe",
#     email="john@example.com",
#     password="hashed_password_here"
# )
# db.add(new_user)
# db.commit()
#
# # User find karna
# user = db.query(User).filter(User.email == "john@example.com").first()


# 📊 MODEL vs SCHEMA:
# Model   → Database table (storage)
# Schema  → API validation (input/output)
# Dono alag hain lekin related!
