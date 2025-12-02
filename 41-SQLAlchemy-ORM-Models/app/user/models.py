# SQLAlchemy ORM imports
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from app.db.base import Base

# User Model - ORM class for users table
class User(Base):
  __tablename__ = "users"  # Table naam

  id: Mapped[int] = mapped_column(primary_key=True)  # Primary key - auto increment
  name: Mapped[str] = mapped_column(String(50), nullable=False)  # User name - required
  email: Mapped[str] = mapped_column(String, nullable=False, unique=True)  # Unique email
  
  def __repr__(self) -> str:
    return f"<User(id={self.id}, name={self.name}, email={self.email})>"  # String representation