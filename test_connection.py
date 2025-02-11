from db_config import engine

try:
    with engine.connect() as conn:
        print("Connection Successful!")
except Exception as e:
    print(f"Connection Failed: {e}")
