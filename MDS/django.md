### proje oluşturma
django-admin startproject websitesi .
### veritabanı onaylamak için 
python manage.py migrate
### süper kullanıcı oluşturmak için
python manage.py createsuperuser
### web sitesi çalıştırmak için
python manage.py runserver
### uygulama oluşturmak için 
python manage.py startapp blog
### veritabanına modeli hazırlamak için
python manage.py makemigrations blog
### veritabanında değişiklikleri onaylamak için
python manage.py migrate