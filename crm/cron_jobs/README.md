# ALX Backend GraphQL CRM Project

## Setup

1. Clone repository
2. Create and activate virtualenv
3. Install dependencies:
   pip install -r requirements.txt
4. Run migrations:
   python manage.py migrate
5. Create superuser:
   python manage.py createsuperuser
6. Run server:
   python manage.py runserver

## Celery

Start worker:
celery -A crm worker -l info

Start beat:
celery -A crm beat -l info

## Crons

Add crontabs:
python manage.py crontab add

List crontabs:
python manage.py crontab show

## GraphQL

Visit:
http://localhost:8000/graphql/

Query:
{
  hello
}
