#!/bin/bash

# Function to display messages
message() {
    echo "====================================="
    echo "$1"
    echo "====================================="
}

# Check if we're running in a virtual environment
if [[ "$VIRTUAL_ENV" == "" ]]; then
    message "Please activate your virtual environment first!"
    exit 1
fi

# Check if git is installed
if ! command -v git &> /dev/null; then
    message "Git is not installed. Please install git first."
    exit 1
fi

# Check for uncommitted changes
if [[ -n $(git status -s) ]]; then
    message "You have uncommitted changes. Please commit them first."
    read -p "Do you want to continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Update requirements
message "Updating requirements.txt"
pip freeze > requirements.txt

# Collect static files
message "Collecting static files"
python manage.py collectstatic --noinput

# Create a lioraxai_project/settings_production.py file if it doesn't exist
if [ ! -f lioraxai_project/settings_production.py ]; then
    message "Creating production settings file"
    cat > lioraxai_project/settings_production.py << 'EOF'
from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']

# Use a more secure secret key in production
SECRET_KEY = 'your-production-secret-key'

# Database settings for production
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'your_db_name',
#         'USER': 'your_db_user',
#         'PASSWORD': 'your_db_password',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

# Email settings for production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
DEFAULT_FROM_EMAIL = 'LioraXAI <your-email@gmail.com>'
EOF
fi

# Git operations
message "Committing changes"
git add .
git commit -m "Deployment update $(date)"

message "Pushing to repository"
git push origin main

message "Deployment preparation complete"
message "Remember to update your server with the latest changes" 