# Base class aur SQLAlchemy types import
from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

# User Model - ORM class
class User(Base):
    __tablename__ = "users"  # Table ka naam

    id: Mapped[int] = mapped_column(primary_key=True)  # Primary key
    name: Mapped[str] = mapped_column(String(50), nullable=False)  # User name
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)  # Unique email
    
    def __repr__(self) -> str:
        return f"<User id={self.id} name={self.name} email={self.email}>"  # Object representation
