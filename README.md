
# FastAPI E-commerce API

This is a **FastAPI-based E-commerce API** using **SQLModel** and **MySQL** to manage **Products and Orders**.

---

## Features
-  CRUD operations for **Products** & **Orders**
-  **SQLModel + MySQL** for database management
-  **Pydantic validation** for request handling
-  **Auto-generated API docs** with Swagger UI

---

## Setup & Installation

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/AshishPython11/fastapi-ecommerce-api.git
cd fastapi-ecommerce-api
```

### **2️⃣ Create a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Configure MySQL Database**
Ensure you have a **MySQL database** set up. Modify **`db_config.py`** with your database credentials:
```python
DB_USERNAME = "your_username"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "ecommerce_db"
```

### **5️⃣ Create Database Tables**
```sh
python create_db.py
```

### **6️⃣ Run the FastAPI Server**
```sh
uvicorn main:app --reload
```
The API will be available at:  
🔹 **http://127.0.0.1:8000**



##  API Documentation
FastAPI automatically generates interactive API documentation:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc UI**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Example API Requests

### **1️⃣ Create a Product**
#### **Request**
```json
POST /products/
{
  "name": "Laptop",
  "description": "High-performance laptop",
  "price": 1299.99
}
```
#### **Response**
```json
{
  "id": 1,
  "name": "Laptop",
  "description": "High-performance laptop",
  "price": 1299.99
}
```

### **2️⃣ Create an Order**
#### **Request**
```json
POST /orders/
{
  "customer_id": 101,
  "product_ids": [1, 2, 3]
}
```
#### **Response**
```json
{
  "id": 1,
  "customer_id": 101,
  "product_ids": "1,2,3",
  "status": "pending"
}
```

---

## Contribution & Support
- If you find any issues, please **open an issue** on GitHub.
- Pull requests are welcome for improvements.

---

## Author
Developed by **Ashish Mishra**  
GitHub: [AshishPython11](https://github.com/AshishPython11)

---

##  License
This project is **open-source** and available under the **MIT License**.

