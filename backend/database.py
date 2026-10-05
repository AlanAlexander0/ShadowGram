import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.models import Base

# Place shadowgram.db in project root or fallback to /tmp if read-only
default_path = Path(__file__).resolve().parent.parent / "shadowgram.db"
db_env = os.getenv("SHADOWGRAM_DB_PATH")
if db_env:
    DB_PATH = Path(db_env)
else:
    try:
        test_file = default_path.parent / ".perm_check"
        test_file.touch()
        test_file.unlink()
        DB_PATH = default_path
    except (PermissionError, OSError):
        DB_PATH = Path("/tmp/shadowgram.db")

DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=False
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Create tables if they don't exist."""
    Base.metadata.create_all(bind=engine)
    print(f"[DB] Initialized SQLite database at: {DB_PATH}")

def get_db():
    """FastAPI dependency for DB session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
