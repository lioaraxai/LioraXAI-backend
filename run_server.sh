#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Apply any pending migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Run server
python manage.py runserver

# To stop the server, press CTRL+C 