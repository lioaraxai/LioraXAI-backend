# Nirdhar - Django Application

This is the Django backend for Nirdhar, an AI-powered knowledge base solution. It works in conjunction with the static marketing website located in the `/Website` directory.

## Project Structure

The project follows a standard Django structure:

- `nirdhar_project/` - Main Django project settings and configuration
- `nirdhar_app/` - Django application containing models, views, and templates
- `staticfiles/` - Collected static files for production
- `manage.py` - Django management script

### Key Components

- **Models** (`nirdhar_app/models.py`): Database models including Contact, Subscriber, and DemoRequest
- **Views** (`nirdhar_app/views.py`): Request handlers including form processing
- **Templates** (`nirdhar_app/templates/`): Django templates for rendering pages
- **Forms** (`nirdhar_app/forms.py`): Form definitions for data validation and processing
- **URLs** (`nirdhar_app/urls.py`): URL routing configuration

## Features

- **Form Processing**: Handles form submissions from both the Django site and the static website
- **Admin Interface**: Django admin panel for managing data
- **Contact Form**: Processes and stores contact form submissions
- **Newsletter Subscriptions**: Manages email newsletter subscriptions
- **Demo Requests**: Processes and tracks demo requests

## Setup Instructions

### Prerequisites

- Python 3.9+
- pip
- virtualenv (recommended)

### Installation

1. Clone the repository (if you haven't already)
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser for the admin panel:
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```
7. Access the site at http://127.0.0.1:8000/

## Integration with Static Website

The Django application is designed to work with the static website located in the `/Website/docs` directory:

- Static website forms submit to Django endpoints
- CSRF protection is temporarily exempted for cross-origin submissions
- Both GET and POST requests are handled for better compatibility

## Form Submission Workflow

1. User fills out a form on the static website
2. Form is submitted to the corresponding Django endpoint (e.g., `/contact/`)
3. Django processes the form data and saves it to the database
4. User is redirected to a success page or shown a success message

## Deployment

For production deployment:

1. Set `DEBUG = False` in `nirdhar_project/settings.py`
2. Configure a proper database (e.g., PostgreSQL)
3. Set up a proper web server (e.g., Nginx + Gunicorn)
4. Configure static file serving
5. Set up proper security measures (HTTPS, proper CSRF handling, etc.)

## Development Guidelines

- Follow PEP 8 style guidelines for Python code
- Run `python manage.py test` before committing changes
- Document any API changes or new features
- Keep model migrations organized and tested

## Recent Updates

- Fixed contact form submission to properly handle POST requests
- Updated form handling in views to process both GET and POST requests
- Implemented CSRF exemption for cross-origin form submissions
- Added better error handling and logging for form submissions

## License

All rights reserved. 