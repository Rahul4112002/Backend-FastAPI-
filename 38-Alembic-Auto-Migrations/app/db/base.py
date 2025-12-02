# SQLAlchemy ORM Base class
from sqlalchemy.orm import DeclarativeBase

# Base class - saare models isse inherit karenge
class Base(DeclarativeBase):
    pass

# Models import karo - Alembic autogenerate ke liye zaroori hai
# Ye imports se Alembic ko pata chalega kaunse models hain
from app.user import models as user_models
from app.product import models as product_models