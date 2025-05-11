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

# Create a superuser if none exists
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'Lioraxai@123!') if not User.objects.filter(username='admin').exists() else print('Admin user already exists')" | python manage.py shell 