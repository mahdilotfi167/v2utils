export PYTHONPATH=.:v2client/v5/proto:$PYTHONPATH
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn --chdir /app v2utils.wsgi:application -w 4 -b :8000