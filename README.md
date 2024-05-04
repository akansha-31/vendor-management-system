# vendor-management-system
This is a Django based Application for Vendor Management System

## Installation

1. Clone the repository
2. Set up a virtual environment
    - python3 -m venv venv
    - source venv/bin/activate

3. Navigate to the project directory - where manage.py is present
    - cd vendor-management-system 
4. Install dependencies by running
    - pip install -r requirements.txt
5. Run Application server by running 
    - python manage.py runserver


## Run APIs

Hit any URL in Browser from below - 
- http://127.0.0.1:8000/admin/
- http://127.0.0.1:8000/api/vendors/
- http://127.0.0.1:8000/api/vendors/<vendor_id>/
- http://127.0.0.1:8000/api/vendors/<vendor_id>/performance/
- http://127.0.0.1:8000/api/purchase_orders/
- http://127.0.0.1:8000/api/purchase_orders/<purchase_order_id>/


# Test Api using postman or curl
    - http://127.0.0.1:8000/api/purchase_orders/<order_id>/acknowledge


## Run Tests

python manage.py test
