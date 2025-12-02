# Base class aur SQLAlchemy types import
from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

# Product Model - ORM class
class Product(Base):
    __tablename__ = "products"  # Table ka naam

    id: Mapped[int] = mapped_column(primary_key=True)  # Primary key
    name: Mapped[str] = mapped_column(String(50), nullable=False)  # Product name - max 50 chars
       
    def __repr__(self) -> str:
        return f"<Product id={self.id} name={self.name}>"  # Object ka string representation
