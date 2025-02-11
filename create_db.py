from db_config import engine
from models import SQLModel

def create_db():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db()
