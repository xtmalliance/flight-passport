#!/bin/bash

# Collect static files
#echo "Collect static files"
#python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate --noinput
echo "Creating superuser.."
python manage.py createsuperuser --noinput
echo "Collecting static"
python manage.py collectstatic
# Start server
echo "Starting server.."
python manage.py runserver 0.0.0.0:8000