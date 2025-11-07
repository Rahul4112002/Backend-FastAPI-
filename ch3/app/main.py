# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                    MAIN.PY - APPLICATION ENTRY POINT                         ║
# ║                    (FastAPI Application Ka Dil)                              ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

# 🔍 YE FILE KYA HAI?
# ===================
# main.py application ka MAIN/ENTRY POINT hai
# Jaise ghar ka main door - sabse pehle yahan se entry hoti hai!
#
# 🎯 PURPOSE (Maksad):
# 1. FastAPI application instance banana
# 2. All routes/routers ko register karna
# 3. Middleware configure karna
# 4. CORS, database connection setup karna
# 5. Application-level settings define karna
#
# 📂 FILE LOCATION:
# ch3/app/main.py
#
# 🚀 KAISE RUN HOTA HAI?
# Command: fastapi dev app/main.py
# Ya: uvicorn app.main:app --reload
#
# 🏗️ TYPICAL STRUCTURE (Aise hoga future mein):
# - Imports (libraries)
# - FastAPI instance creation
# - Database initialization
# - Router registration (user routes, product routes)
# - Middleware setup
# - Root endpoint (/)
# - Error handlers
#
# 💡 WHY SEPARATE MAIN.PY?
# - Clean architecture
# - Easy to find entry point
# - Better organization
# - Testing easier hoti hai


# ┌─────────────────────────────────────────────────────────────────────────────┐
# │  STEP 1: IMPORTS (Future mein aise honge)                                   │
# └─────────────────────────────────────────────────────────────────────────────┘

# from fastapi import FastAPI
# from app.user.routes import router as user_router
# from app.product.routes import router as product_router
# from app.db.config import engine, Base


# ┌─────────────────────────────────────────────────────────────────────────────┐
# │  STEP 2: CREATE FASTAPI INSTANCE                                            │
# └─────────────────────────────────────────────────────────────────────────────┘

# app = FastAPI(
#     title="My API",
#     description="Learning FastAPI Structure",
#     version="1.0.0"
# )


# ┌─────────────────────────────────────────────────────────────────────────────┐
# │  STEP 3: DATABASE SETUP                                                     │
# └─────────────────────────────────────────────────────────────────────────────┘

# Base.metadata.create_all(bind=engine)


# ┌─────────────────────────────────────────────────────────────────────────────┐
# │  STEP 4: REGISTER ROUTERS (Routes ko connect karna)                         │
# └─────────────────────────────────────────────────────────────────────────────┘

# 🔍 ROUTER REGISTRATION:
# - Har module (user, product) ke routes ko yahan register karte hain
# - prefix: URL ke aage lagta hai (e.g., /users, /products)
# - tags: Documentation mein group karne ke liye

# app.include_router(user_router, prefix="/users", tags=["Users"])
# app.include_router(product_router, prefix="/products", tags=["Products"])


# ┌─────────────────────────────────────────────────────────────────────────────┐
# │  STEP 5: ROOT ENDPOINT (Health Check)                                       │
# └─────────────────────────────────────────────────────────────────────────────┘

# @app.get("/")
# def home():
#     return {
#         "message": "Welcome to FastAPI",
#         "version": "1.0.0",
#         "status": "running"
#     }


# ┌─────────────────────────────────────────────────────────────────────────────┐
# │  STEP 6: MIDDLEWARE (Optional - Future mein)                                │
# └─────────────────────────────────────────────────────────────────────────────┘

# from fastapi.middleware.cors import CORSMiddleware
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Production mein specific domains
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                         KEY CONCEPTS                                         ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

# 1. SINGLE RESPONSIBILITY:
#    - main.py sirf application setup karta hai
#    - Business logic alag files mein (routes, services)
#
# 2. ROUTER PATTERN:
#    - Har module ke routes alag file mein
#    - main.py mein sab routers ko include karte hain
#    - Clean aur organized code
#
# 3. SCALABILITY:
#    - Naye modules easily add kar sakte hain
#    - Ek router add karo, include karo, done!
#
# 4. TESTING:
#    - main.py ko test karna easy hai
#    - Mock routers use kar sakte hain


# 💡 BEST PRACTICES:
# ✅ Application configuration yahan rakho
# ✅ All routers ko yahan register karo
# ✅ Global middleware yahan add karo
# ✅ Business logic yahan mat likho (routes/services mein likho)
# ✅ Keep it simple and clean!
