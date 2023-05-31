School Management System

Table of Contents: 1.prerequisites 2.Installation 3.Run the application

prerequisites: install the following prerequisites: 1.python 3.10.4 2.visual studio code

Installation: To set up the School Management System on your local machine, follow the steps below:

1.Navigate to the project directory: cd [project directory] 2.Install the required dependencies: pip install -r requirements.txt 3.run migrations: python manage.py makemigrations python manage.py migrate 4.Configure the database connection and other settings as per your environment.

Run the application: From root directory run:python manage.py runserver

View the application: Go to https://127.0.0.1:8000/ to view the application
