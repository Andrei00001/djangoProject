# djangoProject
И так Привет)
Для запуска понадобится докер(для монги)
Для подключения к бд создаём файлик .env вписываем имя базы данных DATABASE_NAME=

Далее естественно venv, активируем (source ...venv/bin/activate) python 3.10,
устанавливаем зависимости (pip install -r requirements.txt).

Далее python manage.py migrate изначально в бд уже будет записано 2 записи.
Но если будет мало python manage.py createsuperuser, создаем админа, идём в админку после запуска проекта)

Запускаем проект как удобно и возможно) открываем админку (http://127.0.0.1:8000/admin/)

Ну, а дальше собственно в апишке(http://127.0.0.1:8000/api/schema/swagger-ui/#/), либо без апишки (пример:
http://127.0.0.1:8000/get_form/?email=asd@asd.asd&phone=+7 222 222 22 22&date=2023-01-05 )
берем урл отправляем POST запрос вместе с его параметрами и смотрим на ответ)))

Если ничего не сломалось то круть )))

