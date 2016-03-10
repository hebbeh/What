1. Stega in i mappen what
2. cmd "workon env"
3. Stega in i mappen what > what. Starta servern: python manage.py runserver

====================
Övrigt

Requirements - uppdatera
pip freeze > requirements.txt <-- Uppdatera filen

Requirements - installera
pip install -r requirements.txt

Pusha upp till Heroku
https://devcenter.heroku.com/articles/django-app-configuration
Behövs;
- Procfile i rotmappen med web: gunicorn myproject.wsgi --log-file -
- Heroku Toolbelt
- Lägg in gunicorn==19.4.5 i "dependencies"
- dj-database-url
- whitenoise
 