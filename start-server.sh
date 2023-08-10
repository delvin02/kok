#!/usr/bin/env bash

if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd /opt/app/kck; python manage.py createsuperuser --no-input; python manage.py collectstatic --no-input )
fi
(cd /opt/app/kck; gunicorn kck.wsgi --user www-data --bind 0.0.0.0:8000 --workers 3) &
nginx -g "daemon off;"


chmod 755 /opt/app/start-server.sh