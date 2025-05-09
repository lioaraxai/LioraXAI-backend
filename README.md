# LioraXAI - AI-Powered Knowledge Platform

A Django application for LioraXAI, an AI-powered knowledge platform that transforms company knowledge into an interactive chatbot.

## Project Structure

- **lioraxai_project/** - Main Django project settings
- **lioraxai_app/** - Django application with views, templates, and models

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

This project includes several utility scripts to streamline setup and deployment:

- **setup.sh** - Complete project setup script (creates directories, sets up environment, installs dependencies)
- **run_server.sh** - Quick script to activate environment and run the development server
- **run_with_poetry.sh** - Script to run the server using Poetry for dependency management
- **deploy.sh** - Prepares the application for deployment to PythonAnywhere

**IMPORTANT:** Before running any script, check if what you need already exists. The scripts are designed to be idempotent and will check for existing components before creating new ones.

To set up the project quickly:
```
chmod +x setup.sh
./setup.sh
```

To run the server:
```
chmod +x run_server.sh
./run_server.sh
```

## Manual Development Setup

If you prefer a manual setup:

1. Clone the repository:
   ```
   git clone https://github.com/lioraxai/LioraXAI-backend.git
   cd LioraXAI-backend
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

6. Visit http://127.0.0.1:8000/ in your browser

## Using Poetry for Dependency Management

This project supports [Poetry](https://python-poetry.org/) for dependency management. Poetry provides more robust dependency resolution and project management than pip.

### Setting up with Poetry

1. Install Poetry (if not already installed):
   ```
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Make sure Poetry is in your PATH:
   ```
   export PATH="$HOME/.local/bin:$PATH"
   ```

3. Install dependencies using Poetry:
   ```
   poetry install --no-root
   ```

4. Run the Django server with Poetry:
   ```
   poetry run python manage.py runserver 8080
   ```

   Or use the provided script:
   ```
   chmod +x run_with_poetry.sh
   ./run_with_poetry.sh
   ```

5. Visit http://127.0.0.1:8080/ in your browser

### Adding New Dependencies with Poetry

To add a new dependency:
```
poetry add package-name
```

To update dependencies:
```
poetry update
```

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