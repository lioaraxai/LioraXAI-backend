# Nirdhar - AI-Powered Knowledge Base

A Django application for Nirdhar, an AI-powered knowledge base that transforms company knowledge into an interactive chatbot.

## Project Structure

- **nirdhar_project/** - Main Django project settings
- **nirdhar_app/** - Django application with views, templates, and models
- **website/** - Frontend static HTML templates and assets (included in repository)

## Local Development Setup

1. Clone the repository:
   ```
   git clone https://github.com/shardulkulkarni14/nirdhar-backend.git
   cd nirdhar-backend
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

## Features

- **Interactive Chatbot** - AI-powered chatbot to answer questions about company knowledge
- **Contact Form** - Allow users to contact your team
- **Demo Request** - Request demo of the platform
- **Newsletter Subscriptions** - Manage email newsletter subscriptions
- **Dark Mode Support** - Automatically adapts to user's system preferences

## PythonAnywhere Deployment

### Preparation

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

### PythonAnywhere Steps

1. **Sign up/Log in** to PythonAnywhere (https://www.pythonanywhere.com/)

2. **Open a Bash console** from the PythonAnywhere dashboard

3. **Clone the repository**:
   ```
   git clone https://github.com/shardulkulkarni14/nirdhar-backend.git
   cd nirdhar-backend
   ```

4. **Create a virtual environment**:
   ```
   mkvirtualenv --python=python3.10 nirdhar-env
   workon nirdhar-env
   ```

5. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

6. **Collect static files**:
   ```
   python manage.py collectstatic --noinput
   ```

7. **Run migrations**:
   ```
   python manage.py migrate
   ```

8. **Create a Web app** via the PythonAnywhere dashboard:
   - Go to the Web tab
   - Click "Add a new web app"
   - Choose "Manual configuration"
   - Select Python 3.10

9. **Configure the WSGI file**:
   - In the Web tab, find the link to the WSGI configuration file
   - Replace its contents with the contents of `pythonanywhere_wsgi.py`
   - Update the path to match your PythonAnywhere username

10. **Configure static files**:
    - In the Web tab, add a static files mapping:
      - URL: `/static/`
      - Directory: `/home/yourusername/nirdhar-backend/staticfiles`

11. **Configure settings**:
    - Update `nirdhar_project/settings_production.py` with your specific settings
    - Set the environment variable `DJANGO_SETTINGS_MODULE=nirdhar_project.settings_production`

12. **Reload the web app** and visit your site

## Important Files for Deployment

- **deploy.sh** - Script to prepare application for deployment
- **pythonanywhere_wsgi.py** - WSGI configuration for PythonAnywhere
- **nirdhar_project/settings_production.py** - Production settings
- **requirements.txt** - Python package dependencies

## Notes About Static Files

This project combines Django templates with static HTML templates:

- Django templates are in `nirdhar_app/templates/`
- Static assets are in `nirdhar_app/static/`
- The `website/` directory contains the original static HTML site

## Troubleshooting

- If static files aren't loading, check your `STATICFILES_DIRS` setting
- For template errors, verify that the template exists in `nirdhar_app/templates/`
- Check server logs for detailed error information
- Make sure all paths in `pythonanywhere_wsgi.py` match your actual setup

## Maintenance

After deploying, when you need to update your site:

1. Pull the latest changes:
   ```
   cd ~/nirdhar-backend
   git pull
   ```

2. Collect static files and run migrations:
   ```
   python manage.py collectstatic --noinput
   python manage.py migrate
   ```

3. Reload the web app from the PythonAnywhere Web tab 