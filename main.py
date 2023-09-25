from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from pymongo import MongoClient

app = FastAPI()

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce"]
products_collection = db["products"]
orders_collection = db["orders"]


class Product(BaseModel):
    name: str
    price: float
    available_quantity: int


class OrderItem(BaseModel):
    product_id: str
    bought_quantity: int


class UserAddress(BaseModel):
    city: str
    country: str
    zip_code: str


class Order(BaseModel):
    timestamp: datetime
    items: List[OrderItem]
    total_amount: float
    user_address: UserAddress


# Dummy products for reference
dummy_products = [
    Product(name="TV", price=500, available_quantity=10),
    Product(name="Laptop", price=1000, available_quantity=15),
    # Add more dummy products as needed
]


@app.get("/products", response_model=List[Product])
def list_products():
    return dummy_products


@app.post("/orders/", response_model=Order)
def create_order(items: List[OrderItem], user_address: UserAddress):
    total_amount = sum(
        product.price * item.bought_quantity
        for item in items
        for product in dummy_products
        if product.name == item.product_id
    )
    new_order = Order(
        timestamp=datetime.now(),
        items=items,
        total_amount=total_amount,
        user_address=user_address,
    )
    # Save the order to the database (in a real application)
    return new_order


@app.get("/orders/", response_model=List[Order])
def fetch_orders(limit: int = Query(10, le=100), offset: int = Query(0, ge=0)):
    # Fetch orders from the database (in a real application)
    # For now, return dummy orders
    return []


@app.get("/orders/{order_id}", response_model=Order)
def fetch_order(order_id: str):
    # Fetch a single order from the database based on order_id (in a real application)
    # For now, return a dummy order
    return dummy_order


@app.put("/products/{product_id}")
def update_product(product_id: str, new_quantity: int):
    # Update the available quantity of a product in the database (in a real application)
    # For now, update the dummy products
    for product in dummy_products:
        if product.name == product_id:
            product.available_quantity = new_quantity
            return {"message": f"Product {product_id} quantity updated successfully."}
    raise HTTPException(status_code=404, detail="Product not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
