# Database engine aur SQLAlchemy components import karo
from db import engine
from sqlalchemy import MetaData, Table, Column, Integer, String

# Metadata object - tables ki information store karta hai
metadata = MetaData()

# User Table define karo
users = Table(
  "users",  # Table ka naam
  metadata,
  Column("id", Integer, primary_key=True),  # Primary key - unique ID
  Column("name", String(length=50), nullable=False),  # Name - max 50 chars, required
  Column("email", String, nullable=False, unique=True),  # Email - unique hona chahiye
  Column("phone", Integer, nullable=False, unique=True)  # Phone - unique number
  )

# Address Table define karo
address = Table(
  "address",  # Table ka naam
  metadata,
  Column("id", Integer, primary_key=True),  # Primary key
  Column("street", String(length=50), nullable=False),  # Street address
  Column("dist", String, nullable=False, unique=True),  # District - unique
  Column("country", String, nullable=False, unique=True)  # Country - unique
  )

# Tables ko database mein create karne ka function
def create_tables():
  metadata.create_all(engine)  # Saare tables banao

# Tables ko delete karne ka function (commented)
# def drop_tables():
#   metadata.drop_all(engine)  # Saare tables delete karo