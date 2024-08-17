from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./python-fastapi.db"
print("SQLALCHEMY_DATABASE_URL: ", SQLALCHEMY_DATABASE_URL)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True, pool_size=10, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.create_all(bind=engine)

print("Base: ", Base)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
