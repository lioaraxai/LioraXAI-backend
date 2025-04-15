#!/bin/bash

# Make sure submodules are initialized and updated
echo "Updating Git submodules..."
git submodule update --init --recursive

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Make migrations
echo "Making migrations..."
python manage.py makemigrations

# Apply migrations
echo "Applying migrations..."
python manage.py migrate

echo "Deployment preparation complete!"
echo "For PythonAnywhere deployment:"
echo "1. Clone the repository: git clone https://github.com/shardulkulkarni14/nirdhar-backend.git"
echo "2. Initialize submodules: git submodule update --init --recursive"
echo "3. Configure your STATIC_ROOT path in PythonAnywhere's web app settings"
echo "4. Remember to set DEBUG=False in production" 