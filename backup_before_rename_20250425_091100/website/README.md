# LioraXAI Website

This repository contains the website for LioraXAI, an AI-powered knowledge platform solution. The project consists of a static marketing website (in this repository) and a Django application that handles dynamic functionality.

## Project Structure

### Static Website (This Repository)
- Located in the `docs` directory
- Built with HTML, CSS, and JavaScript using Bootstrap 5.3
- Deployed on GitHub Pages
- Forms (like contact form) submit to the Django backend

### Django Application (Separate Repository)
- Located at `/Users/shardulkulkarni/Desktop/Nirdhar/lioraxai_app/`
- Handles dynamic functionality including:
  - Form submissions
  - User authentication
  - Admin panel
  - Database interactions

## Deployment

### Static Website
- Hosted on GitHub Pages at [https://lioaraxai.github.io/LioraXAI](https://lioaraxai.github.io/LioraXAI)
- The `docs` directory serves as the root of the GitHub Pages site

### Django Application
- Requires separate deployment on a server supporting Python/Django
- Currently runs locally for development

## Development Workflow

### Static Website Changes
1. Clone this repository
2. Make changes to the files in the `docs` directory
3. Test locally by opening the HTML files in a browser
4. Commit and push changes to GitHub
5. GitHub Pages will automatically update the live site

### Form Integration with Django
Forms on the static site (like the contact form) are configured to submit to the Django backend:
- Forms use `method="post"` attribute
- Action URLs point to the corresponding Django endpoints (e.g., `/contact/`)
- Django views are configured to handle both GET and POST requests
- Cross-Origin Resource Sharing (CORS) is configured to allow submissions from GitHub Pages

## Recent Updates
- Fixed contact form submission to properly handle POST requests
- Updated form handling in Django views to process both GET and POST requests
- Implemented CSRF exemption for cross-origin form submissions
- Added better error handling and logging for form submissions

## Setup Instructions

### Prerequisites
- Git
- Python 3.9+
- Django 4.2+

### Static Website Setup
```bash
# Clone the repository
git clone https://github.com/lioaraxai/LioraXAI.git
cd LioraXAI

# Open any HTML file in a browser
open docs/index.html
```

### Django Setup
```bash
# Navigate to Django project
cd /path/to/LioraXAI-backend/

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

## License

All rights reserved. 
