from google.cloud.sql.connector import Connector
import sqlalchemy
from sqlalchemy.orm import sessionmaker, declarative_base

# Your Cloud SQL instance connection name
INSTANCE_CONNECTION_NAME = "fastapi-cloudrun-474109:asia-south1:fastapi-sql-instance"

DB_USER = "dbuser"
DB_PASS = "vaishali123"
DB_NAME = "mydb"

def getconn():
    with Connector() as connector:
        conn = connector.connect(
            INSTANCE_CONNECTION_NAME,
            "pg8000",
            user=DB_USER,
            password=DB_PASS,
            db=DB_NAME,
        )
        return conn

engine = sqlalchemy.create_engine(
    "postgresql+pg8000://",
    creator=getconn,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
