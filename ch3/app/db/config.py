# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                   CONFIG.PY - DATABASE CONFIGURATION                         ║
# ║                    (Database Connection Setup)                               ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

# 🔍 YE FILE KYA HAI?
# ===================
# config.py mein DATABASE se related saari configuration hoti hai
#
# 🎯 PURPOSE (Maksad):
# 1. Database connection setup karna
# 2. Database engine create karna
# 3. Session management
# 4. Base class define karna (for models)
#
# 📂 FILE LOCATION:
# ch3/app/db/config.py
#
# 🗄️ KYA HOGA IS FILE MEIN?
# - DATABASE_URL define karna
# - SQLAlchemy engine create karna
# - SessionLocal class (database sessions ke liye)
# - Base class (models inherit karenge isse)
# - get_db() function (dependency injection)


# ┌─────────────────────────────────────────────────────────────────────────────┐
# │  TYPICAL STRUCTURE (Future mein aise hoga)                                  │
# └─────────────────────────────────────────────────────────────────────────────┘

# ============== IMPORTS ==============
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker


# ============== DATABASE URL ==============
# 🔍 Database connection string
# SQLite example: sqlite:///./database.db
# PostgreSQL example: postgresql://user:password@localhost/dbname
#
# DATABASE_URL = "sqlite:///./database.db"


# ============== ENGINE ==============
# 🔍 Database engine - database se connection manage karta hai
# connect_args: SQLite specific setting
#
# engine = create_engine(
#     DATABASE_URL,
#     connect_args={"check_same_thread": False}  # Only for SQLite
# )


# ============== SESSION ==============
# 🔍 SessionLocal - har request ke liye naya session banata hai
# autocommit=False: Manual commit karna padega
# autoflush=False: Manual flush control
# bind=engine: Konsa engine use karna hai
#
# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )


# ============== BASE CLASS ==============
# 🔍 Base - Saare models is class ko inherit karenge
# Ye declarative_base() se aata hai
#
# Base = declarative_base()


# ============== GET DB FUNCTION ==============
# 🔍 Dependency Injection ke liye
# Har request mein fresh database session deta hai
# Try-finally ensure karta hai ki session close ho
#
# def get_db():
#     """
#     Database session dependency
#     Har API request mein use hota hai
#     """
#     db = SessionLocal()
#     try:
#         yield db  # Request ke dauran session use karo
#     finally:
#         db.close()  # Request ke baad session close karo


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                         KEY CONCEPTS                                         ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

# 1. ENGINE:
#    - Database se connection maintain karta hai
#    - Ek baar create hota hai
#    - Saare requests share karte hain
#
# 2. SESSION:
#    - Database operations (CRUD) ke liye
#    - Har request ka apna session hota hai
#    - Transaction management
#
# 3. BASE:
#    - Models ka parent class
#    - Table metadata store karta hai
#    - Migrations ke liye zaroori
#
# 4. GET_DB:
#    - Dependency injection function
#    - Automatic session management
#    - Routes mein Depends(get_db) se use hota hai


# 💡 WHY SEPARATE CONFIG FILE?
# ✅ Database configuration ek jagah hai
# ✅ Reusable across application
# ✅ Easy to modify database settings
# ✅ Testing mein different database use kar sakte hain
# ✅ Environment variables se URL change kar sakte hain


# 🔒 SECURITY TIP:
# DATABASE_URL ko .env file mein store karo
# from dotenv import load_dotenv
# import os
# load_dotenv()
# DATABASE_URL = os.getenv("DATABASE_URL")
