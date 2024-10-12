# **Steps and info in creating django project**

## **Common steps for all projects**
1. Create an environement using conda or python virtual env
2. activate env - conda activate venv/
3. upgrade pip - pip install --upgrade pip
4. create spec(specification/requirements) - deatiled step to complete the project
5. create requirements.txt file - install dependices(pip install -r requirements.txt)

## **Django Setup**
1. Creating a project in django:
   1. `django-admin startproject nameOfProject .` (small letter) - sets up a new django project
   2. cd nameOfProject
   3. `manage.py` helps to write the commands to manage task like working with databases, running servers.
   4. Directory of project contains 4 important files - `settings.py, urls.py, and wsgi.py`(these are most important)
   5. The `settings.py` file controls how Django interacts with your system and manages your project.
   6. The `urls.py` file tells Django which pages to build in response to browser requests
   7. The `(web server gateway interface)wsgi.py` file helps Django serve the files it creates.
   8. `python manage.py runserver` to run the app.

2. Create Databse for sjango to work with:
   1. `python manage.py migrate` - allows to handle administrative and authentication tasks

3. Viewing current state of project:
   1. `python manage.py runserver` - runs app in `development server at http://127.0.0.1:8000/`
   2. `python manage.py runserver 8001` - to run server in differnt server if 8000 in use.
   
4. Starting an App:
   1. open a new terminal - `activate env` and `move to directory.`
   2. `python manage.py startapp app_name` to create a app
   3.  The `most important` files are `models.py, admin.py, and views.py`
   4.  We use `models.py` to define the data we want to manage in our app. 
   5.  admin.py - ``
   6.  views.py - `A view function takes in information from a request, prepares the data needed to generate a page, and then sends the data back to the browser. Itoften does this by using a template that defines what the page will look like.`

5. Defining Models:
      1. write` necessary code to store the data to database`
   
6. Activating model:
   1. open `settings.py` - check `installed apps and add app_name that created.`(app name should be entered before default installed apps - lets you override if needed)

7. Modifting Database to store info from models.py:
   1. `python manage.py makemigrations app_name`- creates a table in database.
   2. applying migration and have the database that has been modified - `python manage.py migrate`
   3. when we want to modify data in app we use this 3 steps:
      1. modify models.py
      2. call makemigrations
      3. migrate

8. Admin Site:
   1. Setting up superuser
      1. `python manage.py createsuperuser`

9. Registering a model in admin site:
   1. open the admins.py file and import dataclass from models.py and register in admin site - admin.site.register(class)
   2. then check http://127.0.0.1:8000/admin - to go to admin panel enter username and password to get in. - allows to add users and groups and manage them.

10. Adding data:
      1. click name which diaplayed under your app to go to the data page
      2. click add topics a form will appear fill it and save

11. Defining the Entry model:
    1.  go to models and modify the code add.

12. Migrate the entry model

13. Registering Entry with the admin site:
    1.  go to admin.py and repeat 9. with proper class
    2.  go to http://127.0.0.1:8000/admin there you can see data
    
14. Django shell - helps for testing project
    1.  python manage.py shell
    2.  ex: - from learning_logs.models import Topic (nextline)Topic.objects.all() it will displays entrys you added
    
15. Creating Home Page:
    1.  Defining url
        1.  Mapping url(urls.py and craete urls.py in app and urls)
    2.  writing views
    3.  writing templates

16. Accounts:
    1. `python manage.py strtapp accounts`
    2. add to settings.py
    3. add url in url patterns

17. Styling and deploying
    1.  pip install django-bootstrap5
    2.  add it in settings apps django_bootstrap5
    3.  style all pages
    4.  Deploy in platform.sh