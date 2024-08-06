Пункты что бы запустить проект:

docker-compose build

docker-compose up

docker-compose exec web python manage.py makemigrations

docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py createsuperuser

И САМОЕ ГЛАВНОЕ ЧТО БЫ У ВАС БЫЛ СВОБОДЕН ПОРТ 5432 ЕСЛИ НЕ ЗАРАБОТАЕТ ТО ИЗМЕНИТЕ ЕГО НА 5433
