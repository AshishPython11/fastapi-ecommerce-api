from sqlmodel import SQLModel, create_engine, Session

# MySQL Database Credentials
DB_USERNAME = "fastapi_user"
DB_PASSWORD = "SV1212"
DB_HOST = "localhost"  # or your MySQL server IP
DB_PORT = "3306"       # Default MySQL port
DB_NAME = "ecommerce_db"

# MySQL Connection String
DATABASE_URL = f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create Engine
engine = create_engine(DATABASE_URL, echo=True)

# Function to Get DB Session
def get_session():
    with Session(engine) as session:
        yield session
