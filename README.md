# Saphora

Saphora E-Commerce Store
Saphora is e-commerce platform built with Django and Django Rest Framework. It provides a solid foundation for creating your own online store, complete with  a robust API to enable seamless integration with your front-end and third-party services.

### Visit site at
https://saphora.onrender.com/

## Features
- User-friendly web interface for customers to browse and purchase products.
- Admin dashboard for managing products, orders, and customer data.
- Extensive API support for developers to extend and customize the platform.
- Secure authentication and authorization system.
- Support for multiple payment gateways.
- Responsive design for mobile and desktop users.

## Installation
### Clone this repository
- git clone https://github.com/Konlan21/Saphora.git
### Create a Virtual environment and activate it
  - python -m venv env
  - env/Scripts/activate
### Install the required dependencies
  - pip  install -r requirements.txt
### Migrate the database
  - python manage.py makemigrations
  - python manage.py migrate
### Create a superuser account
  - python manage.py createsuperuser
### Run the development server
  - python manage.py runserver
