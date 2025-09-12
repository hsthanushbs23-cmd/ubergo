from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ⚠️ replace 'your_password' with your actual postgres password
DATABASE_URL = "postgresql+psycopg2://postgres:#2005REnu@localhost:5432/ride_db"

# Create engine
engine = create_engine(DATABASE_URL)

# Session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
