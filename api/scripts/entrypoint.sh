#!/bin/bash

set -e

python3 manage.py collectstatic --noinput
python3 manage.py migrate --noinput
python3 manage.py initadmin

echo "STARTING GUNICORN SERVER..."
gunicorn config.wsgi:application -t 1800 --bind :8000