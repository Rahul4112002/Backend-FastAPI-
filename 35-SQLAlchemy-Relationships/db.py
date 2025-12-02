# SQLAlchemy engine setup - database connection
from sqlalchemy import create_engine
DATABASE_URL = "sqlite:///sqlite.db"  # SQLite database file path
engine = create_engine(DATABASE_URL, echo=True)  # Engine banao, SQL queries console mein dikhao