Программа для создания видео бегущей строки в формате mp4

Для запуска:

установить виртуальное окружение:
   python -m venv venv
установить библиотеки из файла requirements.txt:
   pip install -r requirements.txt
провести миграции
    python manage.py migrate
запустить приложение
    python manage.py runserver

Работа с приложением:

Создание суперпользователя:
   python manage.py createsuperuser
Пример создания видео:
    http://127.0.0.1:8000?message=Текст сообщения
