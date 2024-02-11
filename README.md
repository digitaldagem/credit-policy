# CREDIT-POLICY
A python service developed using the Django Rest Framework for processing credit policy requests.  

```
credit-policy
    └───src
        └───api
            └───service
                └───policy_check.py
            └───storage
                └───credit_policy.py
                └───serializers.py
            └───transport
                └───urls.py
                └───views.py
        └───core
            └───__init__.py
            └───admin.py
            └───asgi.py
            └───settings.py
            └───wsgi.py
        └───migrations
            └───0001_initial.py
            └───__init__.py
        └───tests
            └───__init__.py
            └───test_post_policy.py
    └───Dockerfile
    └───Makefile
    └───Pipfile
    └───Pipfile.lock
    └───README.md
    └───docker-compose.yml
    └───manage.py
    └───pytest.ini
```

## How to run locally:
* `$ make up`

## How to stop running service:
* `$ make down`

## How to run tests:
Step one create a virtual environment in root directory:
* `$ python3 -m venv .venv`  

Step two activate the virtual environment:
* `$ . .venv/bin/activate`  

Step three install django, djangorestframework, pytest and pytest-django in the virtual environment:
* `$ pip install django djangorestframework pytest pytest-django`  

Step four run pytest
* `$ pytest`


## Endpoint:
Create a new policy:  
`POST :8000/post_policy` 

An example **request payload**:
```json
{
    "customer_income": 1000,
    "customer_debt": 500,
    "payment_remarks_12m": 0,
    "payment_remarks": 1,
    "customer_age": 20
}
```

An example **200 ok** response:
```json
{
    "response": "LOW_INCOME"
}
```

An example **201 created** response:
```json
{
    "response": "ACCEPT"
}
```

2 example **400 bad request** responses:

example 1:
```json
{
    "customer_income": [
        "This field is required."
    ],
    "customer_debt": [
        "This field is required."
    ],
    "payment_remarks_12m": [
        "This field is required."
    ],
    "payment_remarks": [
        "This field is required."
    ],
    "customer_age": [
        "This field is required."
    ]
}
```

example 2:
```json
{
    "customer_income": [
        "A valid integer is required."
    ],
    "customer_debt": [
        "A valid integer is required."
    ],
    "payment_remarks_12m": [
        "A valid integer is required."
    ],
    "payment_remarks": [
        "A valid integer is required."
    ],
    "customer_age": [
        "A valid integer is required."
    ]
}
```
