#!/bin/bash

# Collect static files
#echo "Collect static files"
#python manage.py collectstatic --noinput

# Wait the database to start
echo "Waiting for the database"
sleep 5

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate --noinput
echo "Setting site name"
python manage.py initialize_db
echo "Creating superuser"
python manage.py init_admin
echo "Collecting static"
python manage.py collectstatic --noinput
# Start server
echo "Starting server.."
python manage.py runserver 0.0.0.0:8000
