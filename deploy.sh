#!/bin/bash

# Check if the website directory exists
if [ ! -d "website" ]; then
    echo "Website directory not found. Cloning it..."
    git clone https://github.com/shardulkulkarni14/DocChat.git website
else
    echo "Website directory found. Pulling latest changes..."
    cd website
    git pull
    cd ..
fi

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
echo "2. Clone the website repository: git clone https://github.com/shardulkulkarni14/DocChat.git website"
echo "3. Configure your STATIC_ROOT path in PythonAnywhere's web app settings"
echo "4. Remember to set DEBUG=False in production" 