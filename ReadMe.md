# Lokal Setup (Windows)
Install Python https://www.python.org/downloads/

Check with 'python --version' if install was successful

Run 'pip install virtualenv'

Run 'virtualenv venv', see documentation https://docs.python.org/3/library/venv.html

Run 'venv\Scripts\activate.bat' - 'where python' shows location in directory

Run 'pip install django'

Run 'django-admin startproject taskful_api'

Run '.\manage.py runserver' in folder where manage.py is in folder+

Run '.\manage.py makemigrations' to apply migrations

Run '.\manage.py createsuperuser' to create super user with pw and username/mail