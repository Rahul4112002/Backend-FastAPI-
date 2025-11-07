# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                __init__.py - USER PACKAGE MARKER                             ║
# ║                    (User module ka init file)                                ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

# 🔍 YE FILE KYA HAI?
# ===================
# user folder ko Python PACKAGE banati hai
#
# 📂 FILE LOCATION:
# ch3/app/user/__init__.py
#
# 🎯 PURPOSE:
# - user folder ko package mark karna
# - User module ke components ko import karne ke liye
#
# 📁 USER MODULE MEIN KYA HAI?
# - models.py   → Database table structure
# - schemas.py  → Request/Response validation
# - routes.py   → API endpoints
# - services.py → Business logic
#
# 📝 USAGE:
# from app.user.models import User
# from app.user.routes import router
# from app.user import schemas


# ┌─────────────────────────────────────────────────────────────────────────────┐
# │  FUTURE CODE (Module-level exports)                                         │
# └─────────────────────────────────────────────────────────────────────────────┘

# Agar chahiye to yahan user module ke main components export kar sakte hain
# Example:
# from .models import User
# from .routes import router
# from .schemas import UserCreate, UserResponse
# from .services import UserService
#
# __all__ = ["User", "router", "UserCreate", "UserResponse", "UserService"]


# 💡 WHY THIS STRUCTURE?
# ✅ User se related sab kuch ek jagah
# ✅ Code organization clear hai
# ✅ Naya feature add karna easy
# ✅ Testing aur maintenance simple
