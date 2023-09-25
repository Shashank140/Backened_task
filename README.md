# Ecommerce Backend Application using FastAPI and Python

This is a sample backend application built using FastAPI and Python, simulating an ecommerce system like Flipkart or Amazon.

## Features

- List all available products in the system.
- Create a new order with specified items and user address.
- Fetch all orders from the system with pagination support.
- Fetch a single order based on Order ID.
- Update the available quantity for a product.

## Tech Stack

- Python 3 (3.10 or above)
- FastAPI
- MongoDB with pymongo

## Setup and Installation

1. Clone the repository to your local machine:

   ```bash
   git clone <repository_url>
2. Install the required packages using pip
   ```bash
   pip install -r requirements.txt
3. Run the FastAPI application using Python:
   ```bash
   python main.py

## API Endpoints
List Products:

Endpoint: /products
Method: GET
Description: Get a list of all available products.
Create Order:

Endpoint: /orders
Method: POST
Description: Create a new order with specified items and user address.
Fetch Orders:

Endpoint: /orders
Method: GET
Description: Fetch all orders from the system with pagination support.
Fetch Single Order:

Endpoint: /orders/{order_id}
Method: GET
Description: Fetch a single order based on Order ID.
Update Product Quantity:

Endpoint: /products/{product_id}
Method: PUT
Description: Update the available quantity for a product.
