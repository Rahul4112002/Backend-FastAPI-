# Database aur SQLAlchemy components import
from db import engine
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey

# Metadata - tables ki info store karta hai
metadata = MetaData()

# Users Table - user information
users = Table(
  "users",
  metadata,
  Column("id", Integer, primary_key=True),  # Unique user ID
  Column("name", String(length=50), nullable=False),  # User ka naam
  Column("email", String, nullable=False, unique=True)  # Unique email
  )

# Posts Table - user ke posts
posts = Table(
  "posts",
  metadata,
  Column("id", Integer, primary_key=True),  # Post ID
  Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False),  # Foreign key - user delete ho toh posts bhi delete
  Column("title", String, nullable=False),  # Post title
  Column("content", String, nullable=False),  # Post content
)

# Tables ko database mein create karo
def create_tables():
  metadata.create_all(engine)  # Saare tables banao
