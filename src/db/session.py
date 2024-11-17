from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from src.db.models import Base

DATABASE_URL = "sqlite:///tasks.db"

# Create an engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Scoped session for thread safety in larger applications
db_session = scoped_session(SessionLocal)

# Base for models
Base.metadata.create_all(bind=engine)


def get_db():
    """Dependency that provides a database session."""
    db = db_session()
    try:
        yield db
    finally:
        db.close()
