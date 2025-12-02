# SQLAlchemy ORM import - models banane ke liye
from sqlalchemy.orm import DeclarativeBase

# Base class - saare models isse inherit karenge
class Base(DeclarativeBase):
    pass  # Alembic migrations ke liye metadata yahan se milega