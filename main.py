from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from db_config import get_session
from models import Product, ProductCreate, ProductUpdate, Order, OrderCreate, OrderUpdate

app = FastAPI()

#create product
@app.post("/products/")
def create_product(product: ProductCreate, session: Session = Depends(get_session)):
    db_product = Product(**product.dict())
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product

#get product by id
@app.get("/products/{product_id}")
def get_product(product_id: int, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

#update product by name and description
@app.put("/products/{product_id}")
def update_product(product_id: int, product_data: ProductUpdate, session: Session = Depends(get_session)):
    db_product = session.get(Product, product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    if product_data.name is not None:
        db_product.name = product_data.name
    if product_data.description is not None:
        db_product.description = product_data.description

    session.commit()
    return db_product


#delete product by id
@app.delete("/products/{product_id}")
def delete_product(product_id: int, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    session.delete(product)
    session.commit()
    return {"message": "Product deleted successfully"}

#create order with product ids
@app.post("/orders/")
def create_order(order: OrderCreate, session: Session = Depends(get_session)):
    order_data = Order(
        customer_id=order.customer_id,
        product_ids=",".join(map(str, order.product_ids)) 
    )
    session.add(order_data)
    session.commit()
    session.refresh(order_data)
    return order_data

#get order by id
@app.get("/orders/{order_id}")
def get_order(order_id: int, session: Session = Depends(get_session)):
    order = session.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

#update status
@app.put("/orders/{order_id}/status")
def update_order_status(order_id: int, order_update: OrderUpdate, session: Session = Depends(get_session)):
    order = session.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order.status = order_update.status
    session.commit()
    return order

#delete order by id
@app.delete("/orders/{order_id}")
def delete_order(order_id: int, session: Session = Depends(get_session)):
    order = session.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    session.delete(order)
    session.commit()
    return {"message": "Order deleted successfully"}
