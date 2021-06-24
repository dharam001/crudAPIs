# Project Overview
1. Clone the project
2. Create a virtual environment for the project
       e.g - mkvirtualenv <env name>
       
3. Go to the top project directory named "apiProject" and install require
   packages using cmd :
               pip install -r requirement.txt
               
4. Run migrate command using :
       python manage.py migrate 
       
5. Run server by "python manage.py runserver" command

6. Visiting to server address, Created APIs can be checked.

7. To see the APIs url, go to the "user_app" folder inside project folder and
   in that there is urls.py file which has APIs for required crud operation.
                          OR
       1. http://localhost:8000/   --  List of users
       2. http://localhost:8000/create_user   --  Create user
       3. http://localhost:8000/user/<pk>  -- Get User by id
       4. http://localhost:8000/update/<pk>  -- Update User
       5. http://localhost:8000/delete/<pk>  -- Delete  User
