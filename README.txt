# Создаём виртуальное окружение
& C:/Users/Windows/AppData/Local/Programs/Python/Python310/python.exe -m venv venv

# Активируем venv
venv/Scripts/activate

# Обновляем пакетный менеджер
python -m pip install --upgrade pip

# Устанавливаем фреймворк Django
pip install django

# Создаем проект
django-admin startproject store_project

# Заходим в папку проекта
cd store_project

# Создаем приложения
python manage.py startapp store

# Запускаем сервер
python manage.py runserver

# Операции при изменении базы данных 
python manage.py makemigrations
python manage.py migrate

#
python manage.py createsuperuser
