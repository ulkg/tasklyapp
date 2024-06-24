# Initial Setup (Windows)

- Install Python https://www.python.org/downloads/

- Check with `python --version` if install was successful

- Run `pip install virtualenv`

- Run `virtualenv venv`, see documentation https://docs.python.org/3/library/venv.html

- Run `venv\Scripts\activate.bat` - `where python` shows location in directory

# Project setup

- Run `pip install django`

- Run `django-admin startproject taskful_api` to start a project

- Run `pip install djangorestframework` to install rest framework

- Run `pip install markdown` to install markdown

- Run `pip install django-filter` to install django-filter

- Run `pip install django-rest-framework-social-oauth2` to install module for OAuth2 social authentication support for applications in Django REST Framework.

# Commonly used commands

- Run `python manage.py runserver` in folder where manage.py is in folder

- Run `python manage.py makemigrations` to add migrations to migrations folder

- Run `python manage.py migrate` to apply migrations to db

- Run `python manage.py createsuperuser` to create super user with pw and username/mail



