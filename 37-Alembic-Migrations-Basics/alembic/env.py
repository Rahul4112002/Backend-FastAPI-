# Logging aur SQLAlchemy imports
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from app.db.base import Base  # Base class se metadata milega

# Alembic Config object - alembic.ini file ki values yahan se milti hain
config = context.config

# Logging setup - config file se logger settings load karo
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Target metadata - models ka metadata (autogenerate migrations ke liye zaroori)
# Ye Base.metadata se automatically saare models detect ho jayenge
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


# Offline mode - database connection ke bina migrations generate karo
def run_migrations_offline() -> None:
    """Offline mode mein migrations run karo - sirf SQL script generate hogi
    Database connection nahi banegi, sirf migration files create hongi
    """
    url = config.get_main_option("sqlalchemy.url")  # Database URL config se lo
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()  # Migrations execute karo


# Online mode - database se connect karke migrations run karo
def run_migrations_online() -> None:
    """Online mode - actual database connection banake migrations apply karo
    Database mein changes directly ho jayenge
    """
    # Config se engine create karo
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    # Database connection ke saath migrations run karo
    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata, 
            render_as_batch=True  # SQLite ke liye batch mode
        )

        with context.begin_transaction():
            context.run_migrations()  # Migrations database mein apply karo


# Check karo offline hai ya online mode
if context.is_offline_mode():
    run_migrations_offline()  # Offline mode - sirf SQL generate karo
else:
    run_migrations_online()  # Online mode - database mein apply karo
