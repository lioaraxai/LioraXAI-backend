#!/bin/bash

# Activate the virtual environment
if [ -d "venv" ]; then
source venv/bin/activate
else
    echo "Virtual environment not found. You can create one with: python -m venv venv"
    echo "Then install dependencies with: pip install -r requirements.txt"
fi

# Apply any pending migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Run the development server
python manage.py runserver

# To stop the server, press CTRL+C 