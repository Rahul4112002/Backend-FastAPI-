# SQLAlchemy async imports - asynchronous database operations ke liye
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import os

# Base directory path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(BASE_DIR)

# Database file path
db_path= os.path.join(BASE_DIR, "sqlite.db")

# Database URL - aiosqlite driver for async operations
DATABASE_URL = f"sqlite+aiosqlite:///{db_path}"

# Async Engine - non-blocking database connection
engine = create_async_engine(DATABASE_URL, echo=True)  # echo=True - queries print hongi

# Async Session factory - async database operations ke liye
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)