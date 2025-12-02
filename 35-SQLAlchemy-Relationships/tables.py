# Database aur SQLAlchemy components import
from db import engine
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey

# Metadata - tables ki info store karta hai
metadata = MetaData()

# Users Table - main user information
users = Table(
  "users",
  metadata,
  Column("id", Integer, primary_key=True),  # Unique user ID
  Column("name", String(length=50), nullable=False),  # User ka naam
  Column("email", String, nullable=False, unique=True),  # Unique email
  Column("phone", Integer, nullable=False, unique=True)  # Unique phone number
  )

# Posts Table - One to Many relationship (ek user ke kai posts ho sakte hain)
posts = Table(
  "posts",
  metadata,
  Column("id", Integer, primary_key=True),  # Post ID
  Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False),  # Foreign key - user delete ho toh posts bhi delete
  Column("title", String, nullable=False),  # Post ka title
  Column("content", String, nullable=False),  # Post content
)

# Profile Table - One to One relationship (ek user ka ek hi profile)
profile = Table(
  "profile",
  metadata,
  Column("id", Integer, primary_key=True),  # Profile ID
  Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True),  # Unique foreign key - sirf ek profile per user
  Column("bio", String, nullable=False),  # Bio text
  Column("address", String, nullable=False),  # Address
)

# Address Table - Many to Many ke liye
address = Table(
  "address",
  metadata,
  Column("id", Integer, primary_key=True),  # Address ID
  Column("street", String, nullable=False),  # Street name
  Column("country", String, nullable=False),  # Country
)

# Association Table - Many to Many relationship (ek user ke kai addresses, ek address ke kai users)
user_address_association = Table(
  "user_address_association",
  metadata,
  Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),  # User foreign key
  Column("address_id", Integer, ForeignKey("address.id", ondelete="CASCADE"), primary_key=True),  # Address foreign key
)



# Tables ko database mein create karo
def create_tables():
  metadata.create_all(engine)  # Saare tables relationships ke saath banao
