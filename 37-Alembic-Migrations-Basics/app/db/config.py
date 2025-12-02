# SQLAlchemy imports - database connection ke liye
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Base directory path nikalo (project ka root folder)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(BASE_DIR)

# SQLite database file ka path banao
db_path= os.path.join(BASE_DIR, "sqlite.db")

# Database URL - sqlite database file ka location
DATABASE_URL = f"sqlite:///{db_path}"

# Engine create karo - database connection handle karta hai
engine = create_engine(DATABASE_URL, echo=True)  # echo=True se SQL queries console mein dikhte hain

# Session factory - database operations ke liye sessions banata hai
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)