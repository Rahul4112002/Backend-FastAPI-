# Tables aur services import karo
from tables import create_tables
from services import *

# Database tables create karo
create_tables()  # Tables ko database mein banao

# Naya user add karo - Create operation
# create_user("sonam", "sonam@example.com")
# create_user("raj", "raj@example.com")
# create_post(1, "Hello World", "This is Sonam's first post")
# create_post(2, "Raj's Post", "Hi from Raj!")

# Data fetch karo - Read operations
# print(get_user_by_id(1))
# print(get_all_users())
# print(get_posts_by_user(2))

# Data update karo - Update operation
# update_user_email(1, "sonam@newdomain.com")

# Data delete karo - Delete operation
# delete_post(2)