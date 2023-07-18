#!/bin/bash

# Default values
SHOWLOGS=false

# Parse command line options
while [[ $# -gt 0 ]]
do
key="$1"
case $key in
    --logs)
    SHOWLOGS=true
    shift
    ;;
    *)
    shift
    ;;
esac
done

echo "Stopping previous Sass watcher..."
pkill -9 -f sass

echo "Starting new Sass watcher F5 ROOT ..."
sass --watch /home/django/firstfiverugby/f5/static/scss:/home/django/firstfiverugby/f5/static/css &

echo "Starting new Sass watcher MEMBERS ..."
sass --watch /home/django/firstfiverugby/members/static/scss:/home/django/firstfiverugby/members/static/css &

echo "Starting new Sass watcher CATALOG ..."
sass --watch /home/django/firstfiverugby/catalog/static/scss:/home/django/firstfiverugby/catalog/static/css &

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Restarting gunicorn and nginx..."
sudo systemctl restart gunicorn.service
sudo systemctl restart nginx.service

if $SHOWLOGS ; then
    echo "Showing logs for gunicorn and nginx..."
    journalctl -u gunicorn.service -n 50 --no-pager
    journalctl -u nginx.service -n 50 --no-pager
else
    echo "Status of gunicorn and nginx..."
    sudo systemctl status gunicorn.service
    sudo systemctl status nginx.service
fi
