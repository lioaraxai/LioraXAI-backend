# LioraXAI - AI-Powered Knowledge Platform

A Django application for LioraXAI, an AI-powered knowledge platform that transforms company knowledge into an interactive chatbot.

## Project Structure

- **lioraxai_project/** - Main Django project settings
- **lioraxai_app/** - Django application with views, templates, and models
  - **templates/** - HTML templates using Django template language
  - **static/** - CSS, JavaScript, and image files
  - **views.py** - View functions handling requests and responses
  - **models.py** - Database models
  - **urls.py** - URL routing configurations
  - **forms.py** - Form definitions and validation
- **staticfiles/** - Collected static files for production (generated)
- **manage.py** - Django's command-line utility for administrative tasks
- **requirements.txt** - Python package dependencies
- **pyproject.toml** - Poetry configuration for dependency management

## No Frontend Dependencies Required

This project has been designed to work without requiring a separate frontend repository. The `setup.sh` script:

1. Creates minimal static files needed for basic functionality
2. Configures the application with essential CSS, JavaScript, and placeholder images
3. Allows you to optionally include a frontend repository if needed

To use without the frontend repository:
```
chmod +x setup.sh
./setup.sh
```

To include the frontend repository (optional):
```
chmod +x setup.sh
./setup.sh --with-website
```

## Quick Setup with Scripts

This project uses Poetry for dependency management and includes a few utility scripts:

- **run.sh** - Quick script to run the development server using Poetry
- **build.sh** - Used for deployment on Render.com
- **deploy.sh** - Prepares the application for deployment to PythonAnywhere

To run the development server:
```
chmod +x run.sh
./run.sh  # Runs on port 8000 by default
./run.sh 8080  # Specify a different port
```

## Manual Development Setup

If you prefer a manual setup:

1. Clone the repository:
   ```
   git clone https://github.com/lioraxai/LioraXAI-backend.git
   cd LioraXAI-backend
   ```

2. Install Poetry (if not already installed):
   ```
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. Install dependencies using Poetry:
   ```
   poetry install
   ```

4. Run migrations:
   ```
   poetry run python manage.py migrate
   ```

5. Run the development server:
   ```
   poetry run python manage.py runserver
   ```

6. Visit http://127.0.0.1:8000/ in your browser

## Using Poetry for Dependency Management

This project uses [Poetry](https://python-poetry.org/) for dependency management.

### Adding New Dependencies with Poetry

To add a new dependency:
```
poetry add package-name
```

To update dependencies:
```
poetry update
```

### The requirements.txt File

A `requirements.txt` file is maintained for compatibility purposes only. The primary source of truth for dependencies is the `pyproject.toml` file.

## Features

- **Interactive Chatbot** - AI-powered chatbot to answer questions about company knowledge
- **Contact Form** - Allow users to contact your team
- **Demo Request** - Request demo of the platform
- **Newsletter Subscriptions** - Manage email newsletter subscriptions
- **Dark Mode Support** - Automatically adapts to user's system preferences

## PythonAnywhere Deployment

For detailed PythonAnywhere deployment instructions, see [PYTHONANYWHERE_DEPLOY.md](PYTHONANYWHERE_DEPLOY.md).

### Quick Deployment Steps

1. Make sure your code is committed and pushed to GitHub:
   ```
   git add .
   git commit -m "Prepare for deployment"
   git push
   ```

2. Run the deployment preparation script:
   ```
   chmod +x deploy.sh
   ./deploy.sh
   ```

3. Follow the instructions provided by the deployment script for setting up on PythonAnywhere.

## Important Files for Deployment

- **deploy.sh** - Script to prepare application for deployment
- **pythonanywhere_wsgi.py** - WSGI configuration for PythonAnywhere
- **lioraxai_project/settings_production.py** - Production settings
- **requirements.txt** - Python package dependencies

## Notes About Static Files

This project includes minimal static files directly in the backend:

- Minimal responsive CSS with dark mode support
- Basic JavaScript functionality
- Placeholder images for essential UI elements
- All files are located in `lioraxai_app/static/`

## Development Guidelines

1. **Check Before Creating**: Always check if a file, directory, or functionality already exists before creating it new.
2. **Use Existing Scripts**: Use the provided scripts for common tasks rather than creating new ones.
3. **Document Changes**: When adding new files or functionality, update the README or other documentation.
4. **Follow Conventions**: Maintain the existing project structure and naming conventions.

## Troubleshooting

- If static files aren't loading, check your `STATICFILES_DIRS` setting
- For template errors, verify that the template exists in `lioraxai_app/templates/`
- Check server logs for detailed error information
- Make sure all paths in `pythonanywhere_wsgi.py` match your actual setup

## Maintenance

After deploying, when you need to update your site:

1. Pull the latest changes:
   ```
   cd ~/LioraXAI-backend
   git pull
   ```

2. Collect static files and run migrations:
   ```
   python manage.py collectstatic --noinput
   python manage.py migrate
   ```

3. Reload the web app from the PythonAnywhere Web tab 