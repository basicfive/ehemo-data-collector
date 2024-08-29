from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.core.config import settings
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()