# database.py

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Supabase PostgreSQL connection URL (from environment variable)
DATABASE_URL = os.getenv("SUPABASE_POSTGRES_URL_NON_POOLING")

# Create async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Session
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base model
Base = declarative_base()

# Dependency to get DB session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
