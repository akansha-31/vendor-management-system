# vendor-management-system
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
This is a Django based Application for Vendor Management System

# Installation

1. Clone the repository
2. Set up a virtual environment
    - python3 - m venv venv
    - source venv/bin/activate

3. Navigate to the project directory - where manage.py is present
    - cd vendor-management-system
4. Install dependencies by running
    - pip install - r requirements.txt
5. Run Application server by running
    - python manage.py runserver


# create a superuser
- python manage.py createsuperuser


# Create Tokens for User
By default, DRF doesn't create tokens automatically. You need to create tokens for users manually. You can do this using Django's shell

1. open shell by running -
    - python manage.py shell

2. create token for user
    - user = User.objects.get(username='your_username')
    - token = Token.objects.create(user=user)


# Use token in postman
1. Add header with key "Authorization" and value "Token < Token >"
2. Replace < Token > with the generated token from the previous step.


# Test Api using postman
- http: // 127.0.0.1: 8000/api/vendors/
- http: // 127.0.0.1: 8000/api/vendors/<vendor_id > /
- http: // 127.0.0.1: 8000/api/vendors/<vendor_id > /performance/
- http: // 127.0.0.1: 8000/api/purchase_orders/
- http: // 127.0.0.1: 8000/api/purchase_orders/<purchase_order_id > /
- http: // 127.0.0.1: 8000/api/purchase_orders/<order_id > /acknowledge


# Access Admin Page in Browser
- http: // 127.0.0.1: 8000/admin/


# API Docs
- http: // 127.0.0.1: 8000/api/docs


# Run Tests

python manage.py test
