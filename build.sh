#!/bin/bash

# Exit on error
set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

# Run setup script (without website since we'll use the included static files)
echo "Running setup script..."
chmod +x setup.sh
./setup.sh

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run migrations forcefully (with verbose output)
echo "Running migrations with verbose output..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput --verbosity 2

# Create a superuser if none exists
echo "Attempting to create admin user..."
cat << EOF | python manage.py shell
from django.contrib.auth.models import User
from django.db import connection

# First check if auth_user table exists
with connection.cursor() as cursor:
    try:
        cursor.execute('''
            SELECT EXISTS (
               SELECT FROM information_schema.tables 
               WHERE table_schema = 'public'
               AND table_name = 'auth_user'
            );
        ''')
        table_exists = cursor.fetchone()[0]
        
        if not table_exists:
            print("Auth_user table doesn't exist. Running migrations again...")
            from django.core.management import call_command
            call_command('migrate', 'auth')
            call_command('migrate')
    except Exception as e:
        print(f"Error checking auth_user table: {e}")

try:
    if User.objects.filter(username='admin').exists():
        print("Admin user already exists")
    else:
        User.objects.create_superuser('admin', 'admin@example.com', 'Lioraxai@123!')
        print("Admin user created successfully")
except Exception as e:
    print(f"Error creating user: {e}")
EOF

echo "Build completed!" 