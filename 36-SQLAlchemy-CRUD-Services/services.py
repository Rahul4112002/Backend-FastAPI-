# Database aur tables import karo
from db import engine
from tables import users, posts
from sqlalchemy import insert, select, update, delete

# Naya user create karo - INSERT operation
def create_user(name: str, email: str):
  with engine.connect() as conn:  # Database connection open karo
    stmt = insert(users).values(name=name, email=email)  # INSERT statement banao
    conn.execute(stmt)  # Query execute karo
    conn.commit()  # Changes save karo

# Naya post create karo - INSERT operation
def create_post(user_id: int, title: str, content: str):
    with engine.connect() as conn:
        stmt = insert(posts).values(user_id=user_id, title=title, content=content)
        conn.execute(stmt)
        conn.commit()

# User ko ID se fetch karo - SELECT operation
def get_user_by_id(user_id: int):
   with engine.connect() as conn:
        stmt = select(users).where(users.c.id == user_id)  # WHERE clause ke saath SELECT
        result = conn.execute(stmt).first()  # Pehla row return karo
        return result
   
# Saare users fetch karo - SELECT operation
def get_all_users():
   with engine.connect() as conn:
        stmt = select(users)  # Saare users select karo
        result = conn.execute(stmt).fetchall()  # Saari rows return karo
        return result
   
# User ke posts fetch karo - SELECT with WHERE
def get_posts_by_user(user_id: int):
   with engine.connect() as conn:
        stmt = select(posts).where(posts.c.user_id == user_id)  # User ID se filter karo
        result = conn.execute(stmt).fetchall()
        return result
   
# User ka email update karo - UPDATE operation
def update_user_email(user_id: int, new_email: str):
   with engine.connect() as conn:
        stmt = update(users).where(users.c.id == user_id).values(email=new_email)  # UPDATE with WHERE
        conn.execute(stmt)
        conn.commit()

# Post delete karo - DELETE operation
def delete_post(post_id: int):
   with engine.connect() as conn:
        stmt = delete(posts).where(posts.c.id == post_id)  # DELETE with WHERE
        conn.execute(stmt)
        conn.commit()