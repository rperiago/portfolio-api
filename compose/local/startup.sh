#!/bin/bash

python wait_mysql.py

python manage.py collectstatic -c --noinput

python manage.py migrate



gunicorn base.wsgi -b 0.0.0.0:8000 --reload --log-level=DEBUG --timeout 2200 -w 4 -k gevent

