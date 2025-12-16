import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# For Vercel serverless, use /tmp which is writable
# For local dev, use current directory
DB_PATH = os.getenv("DATABASE_URL", "sqlite:///./shardium.db")

# Handle Vercel's /tmp directory for SQLite
if os.getenv("VERCEL"):
    DB_PATH = "sqlite:////tmp/shardium.db"

engine = create_engine(
    DB_PATH, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

