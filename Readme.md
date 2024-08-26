# step 1: creating a virtual environment : python -m venv myenv
# step 2 activate virtual environment   : for cmd myenv\Scripts\activate for powershell or bash: myenv/Scripts/activate
# step 3: install packages : pip install django flask check for installed packages: pip list
# step 4: add install package in requirements.txt  :  pip freeze > requirements.txt
# step 5: checking if install django and flask is properly installed : django-admin --version and flask --version
# step 6: start django project: django-admin startproject StudentForm .
# step 7: create modules(sub project) for different features : python manage.py startapp Student
# step 8: config sub project in main project
# step 9: migrate to create database i.e python manage.py migrate
# step 10: createsuperuser and run server e.g python manage.py createsuperuser and python manage.py runserver


