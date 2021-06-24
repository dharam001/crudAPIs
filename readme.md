## CRUD in Django REST framework
This is a small Django project to demonstrate Django CRUD functionality.

### Prerequisites
Python 3.9+ [Download](https://www.python.org/downloads/)

Django 3.2+

Django REST Framework 3.1+

### Installation
Clone project
`git clone https://github.com/dharam001/crudAPIs.git`
   
Create a virtual environment for the project (windows)
   
   `pip install virtualenvwrapper-win`
   
   `mkvirtualenv <env name>`
       
Install required packages using command :
   
   `cd apiProject`
   
   `pip install -r requirement.txt`
               
### Running the Application
Before running the application we need to create the needed DB tables:

`python manage.py migrate`

Now you can run the development web server:

`python manage.py runserver`

To access the applications go to the URL http://localhost:8000/
       
### Visit `urls.py` in users_app to test APIs
     
### List of APIs
       http://localhost:8000/   --  List of users
       http://localhost:8000/create_user   --  Create user
       http://localhost:8000/user/<pk>  -- Get User by id
       http://localhost:8000/update/<pk>  -- Update User
       http://localhost:8000/delete/<pk>  -- Delete  User

### Running Testcases
Run all testcases inside project

`cd apiProject`
  
`pytest -v`
  
Running individual test

`cd apiProject`

`pytest -v <app-name>/<test folder>/<file-name>::<class name>::<method name>`