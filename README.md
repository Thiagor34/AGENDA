# AGENDA


python -m venv venv

.\venv\Scripts\activate (para entrar novamente, caso saia do cmd)

pip install django

pip freeze > requirements.txt 

python -m django startproject agenda .

python manage.py runserver (rodar servidor)

python manage.py startapp contatos

python manage.py makemigrations 

python manage.py migrate

python manage.py createsuperuser

python manage.py shell

