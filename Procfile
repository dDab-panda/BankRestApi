release: python manage.py collectstatic --noinput
web: gunicorn bankApi.wsgi:application --log-file - --log-level debug

