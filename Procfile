
web: gunicorn  --bind=0.0.0.0:$PORT  intros.wsgi:application  --log-file -
worker: python manage.py celeryd -E -B --loglevel=INFO
