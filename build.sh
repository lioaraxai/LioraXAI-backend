#!/bin/bash

# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Run setup script (without website since we'll use the included static files)
chmod +x setup.sh
./setup.sh

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate 