# SQLAlchemy engine import karo
from sqlalchemy import create_engine

# Database URL - SQLite file path
DATABASE_URL = "sqlite:///./sqlite.db"

# Engine create karo - database connection ke liye
# echo=True - SQL queries console mein print honge (debugging ke liye)
engine = create_engine(DATABASE_URL, echo=True)