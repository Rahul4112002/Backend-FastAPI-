# SQLAlchemy ORM imports
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from app.db.base import Base

# Product Model - ORM class for products table
class Product(Base):
  __tablename__ = "products"  # Table naam

  id: Mapped[int] = mapped_column(primary_key=True)  # Primary key
  name: Mapped[str] = mapped_column(String(50), nullable=False)  # Product name
  
  def __repr__(self) -> str:
    return f"<Product(id={self.id}, name={self.name})>"  # String representation