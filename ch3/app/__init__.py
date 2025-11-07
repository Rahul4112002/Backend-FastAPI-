# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                    __init__.py - PACKAGE MARKER FILE                         ║
# ║                         (app folder ka init file)                            ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

# 🔍 YE FILE KYA HAI?
# ===================
# __init__.py (dunder init) ek SPECIAL file hai Python mein
#
# 🎯 PURPOSE (Maksad):
# 1. Is folder ko Python PACKAGE banati hai
# 2. Bina is file ke, Python ye folder ko package nahi maanta
# 3. Isme package-level initialization code likh sakte hain
#
# 📂 FILE LOCATION:
# ch3/app/__init__.py
#
# 🤔 PACKAGE KYA HAI?
# Package = Folder jisme __init__.py file ho
# Isse hum isko import kar sakte hain:
# from app import something
# from app.user import models
#
# 📝 YE FILE EMPTY KYU HAI?
# - Agar koi initialization code nahi chahiye, to empty rakh sakte hain
# - Sirf folder ko package mark karne ke liye enough hai
#
# 🔧 AGAR CODE LIKHNA HO TO KYA LIKHENGE?
# Example:
# from .main import app
# from .db.config import get_db
#
# __all__ = ["app", "get_db"]
#
# 💡 REMEMBER:
# - Har folder jo package banana chahte ho, usme __init__.py chahiye
# - Ye file empty bhi ho sakti hai
# - Python 3.3+ mein ye optional hai (namespace packages)
# - But best practice hai ye file rakhna!


# ┌─────────────────────────────────────────────────────────────────────────────┐
# │  INITIALIZATION CODE (Agar future mein chahiye)                             │
# └─────────────────────────────────────────────────────────────────────────────┘

# Yahan package-level imports aur configuration aa sakta hai
# Abhi ke liye empty rakha hai
