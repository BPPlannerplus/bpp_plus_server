#!/bin/sh

python manage.py collectstatic --no-input
python manage.py crontab add
python manage.py migrate

exec "$@"
