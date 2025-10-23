# djangoserver
python3 -m venv venv        
source venv/bin/activate    

pip install django          

django-admin startproject myproject
cd myproject

python manage.py runserver

python manage.py startapp myapp

python manage.py migrate


pip install -r requirements.txt # install dependencies

pip freeze > requirements.txt # update dependencies
