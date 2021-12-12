# course_api

#### Установка:
1. Клонируйте репозиторий
2. Создайте и войдите в вирутальное окружение
3. Установите зависимости:
    - `pip install -r requirements.txt`
4. Добавить секретный ключ
5. Добавить почту для рассылки
6. Проведите миграции
    - `python manage.py makemigrations`
    - `python manage.py migrate`
7. Запустите тестовый сервер
    - `python manage.py runserver`