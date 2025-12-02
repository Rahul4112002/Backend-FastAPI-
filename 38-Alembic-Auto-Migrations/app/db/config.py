# SQLAlchemy imports - database connection ke liye
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Base directory path nikalo
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(BASE_DIR)

# Database file path
db_path= os.path.join(BASE_DIR, "sqlite.db")

# Database URL
DATABASE_URL = f"sqlite:///{db_path}"

# Engine - database connection
engine = create_engine(DATABASE_URL, echo=True)

# Session factory - database operations ke liye
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)