#!/usr/bin/env bash

python manage.py migrate

python manage.py initadmin

ls

ls /usr/src/epam

gunicorn epam.wsgi:application --bind 0.0.0.0:8000 --reload -w 2