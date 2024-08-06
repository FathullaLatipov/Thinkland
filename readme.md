Пункты что бы запустить проект:

python3 -m venv venv

MACOS - source venv/bin/activate
Windows - venv/Scripts/activate

docker-compose build

docker-compose up

docker-compose exec web python manage.py makemigrations

docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py createsuperuser

И САМОЕ ГЛАВНОЕ ЧТО БЫ У ВАС БЫЛ СВОБОДЕН ПОРТ 5432 ЕСЛИ НЕ ЗАРАБОТАЕТ ТО ИЗМЕНИТЕ ЕГО НА 5433


Что бы использовать Elasticsearch надо отправить запрос в таком формате
Например:
/api/search/?q=Product1 