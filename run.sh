export PYTHONPATH=.:v2client/v5/proto:$PYTHONPATH
#check if $V2ENV is equal to "prod"
if [ "$V2ENV" = "prod" ]; then
    echo "Running in production mode"
    python manage.py migrate
    python manage.py collectstatic --noinput
    gunicorn --chdir /app v2utils.wsgi:application -w 4 -b :8000
else
    echo "Running in development mode"
    python manage.py migrate
    python manage.py runserver 0.0.0.0:8000
fi