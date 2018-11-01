# shopers_store_api_2
[![Build Status](https://travis-ci.org/araaliFarooq/shopers_store_api_2.svg?branch=challenge_3)](https://travis-ci.org/araaliFarooq/shopers_store_api_2)
[![Coverage Status](https://coveralls.io/repos/github/araaliFarooq/shopers_store_api_2/badge.svg?branch=challenge_3)](https://coveralls.io/github/araaliFarooq/shopers_store_api_2?branch=challenge_3)[![Codacy Badge](https://api.codacy.com/project/badge/Grade/64cbe570b5c34e6f9e587f655c6b276a)](https://www.codacy.com/app/araaliFarooq/shopers_store_api_2?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=araaliFarooq/shopers_store_api_2&amp;utm_campaign=Badge_Grade)

## About
This is an API of an application to manage and record transcations of a shopping store

## Heroku demo link
- https://shopers-store-api-2.herokuapp.com/

## API Documentation
- https://araalifarooq.docs.apiary.io

## Features
- Login
- Create an attendant's account
- Fetch all products
- Fetch a single product record
- Fetch all sale records
- Fetch a single sale record
- Create a product
- Create a sale order
- Update a prooduct item
- Delete a product item

## Other features
- Update the role of an attendant

## Tools Used
- [Flask](http://flask.pocoo.org/) - web microframework for Python
- [PostgreSQL](https://www.postgresql.org/)- Open source relational database

## Requirements
Python 3.6.x+

## Run (Use) on your local machine
First clone the repository
```sh
   $ git clone https://github.com/araaliFarooq/shopers_store_api_2
   ```
   Head over to the cloned directory, create a virtual environment, use pip to install the requirements, then run the app
   ```
    $ cd shopers_store_api_2
    $ virtualenv env
    $ source env/bin/activate
    $ pip install -r requirements.txt
    $ python run.py
```
## Runtime environment variable configs for TESTS
```
    $ Set APP_SETTINGS to TESTING
```
## Runtime environment variable configs for DEVELOPMENT
```
    $ Set APP_SETTINGS to DEVELOPMENT
    $ Set values of your choice for dbname, host, user, password and port for the PostgreSQL database
```

#### Endpoints to create an attendants account and login into the application
HTTP Method|End point | Public Access|Action
-----------|----------|--------------|------
POST | /api/auth/register | False | Create an attendant's account
POST | /api/auth/login | True | Login a user

#### Endpoints to create, views available products and create sale records
HTTP Method|End point | Public Access|Action
-----------|----------|--------------|------
POST | /api/v2/products | False | Create a product
POST | /api/v2/sales | False | Create a sale order
GET | /api/v2/products | False | Fetch all available products
GET | /api/v2/products/<product_id> | False | Fetch details of a single product
DELETE | /api/v2/products/<product_id> | False | Delete a single product
PUT | /api/v2/products/<product_id> | False | Edit details of a single product
GET | /api/v2/sales/<sale_id> | False | Fetch details of a single sale record
GET | /api/v2/sales | False | Fetch all sale records created
PUT | /api/auth/users | False | Change the role of an attendant

## Authors
[Araali Sseruwu Farooq](https://github.com/araalifarooq)
