#!/bin/bash

# Default values
SHOWLOGS=false
PROJECT_PATH=/home/django/firstfiverugby

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

echo "Starting new Sass watchers..."
# Find all 'scss' directories in the project
for SCSS_DIR in $(find $PROJECT_PATH -type d -name 'scss'); do
    # Get the parent directory of the current 'scss' directory to use as the 'css' directory
    CSS_DIR="${SCSS_DIR/scss/css}"

    # Start a new Sass watcher for the current 'scss' directory
    sass --watch $SCSS_DIR:$CSS_DIR &
done

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
