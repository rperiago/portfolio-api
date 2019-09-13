#!/bin/bash
python3 wait_mysql.py
python3 manage.py collectstatic -c --noinput
python3 manage.py --settings=base.production
gunicorn base.wsgi -b 0.0.0.0:8000 --reload --log-level=DEBUG --timeout 2200 -w 4 -k gevent
