Create virtual environment: python3 -m venv demo-project-env

Activate virtual environment : source demo-project-env/bin/activate

Install requirements : pip install -r requirements.txt

To run django server : python manage.py runserver 0.0.0.0:8000

To run celery : celery -A demoproject worker --loglevel=info