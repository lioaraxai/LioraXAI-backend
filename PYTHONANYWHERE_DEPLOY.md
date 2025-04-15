# Deploying to PythonAnywhere

This guide will help you deploy the Nirdhar application on PythonAnywhere.

## Pre-deployment Setup

1. Run the deployment script locally to verify everything works:
   ```
   ./deploy.sh
   ```

## PythonAnywhere Deployment Steps

1. **Sign up/Log in** to PythonAnywhere (https://www.pythonanywhere.com/)

2. **Open a Bash console** from the PythonAnywhere dashboard

3. **Clone the repository**:
   ```
   git clone https://github.com/shardulkulkarni14/nirdhar-backend.git
   cd nirdhar-backend
   ```

4. **Clone the website repository**:
   ```
   git clone https://github.com/shardulkulkarni14/DocChat.git website
   ```

5. **Create a virtual environment**:
   ```
   mkvirtualenv --python=python3.10 nirdhar-env
   workon nirdhar-env
   ```

6. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

7. **Collect static files**:
   ```
   python manage.py collectstatic --noinput
   ```

8. **Run migrations**:
   ```
   python manage.py migrate
   ```

9. **Create a Web app** via the PythonAnywhere dashboard:
    - Go to the Web tab
    - Click "Add a new web app"
    - Choose "Manual configuration"
    - Select Python 3.10

10. **Configure the WSGI file**:
    - In the Web tab, find the link to the WSGI configuration file
    - Replace its contents with the contents of `pythonanywhere_wsgi.py`
    - Update the path to match your PythonAnywhere username

11. **Configure static files**:
    - In the Web tab, add a static files mapping:
      - URL: `/static/`
      - Directory: `/home/yourusername/nirdhar-backend/staticfiles`

12. **Set environment variables**:
    - In the Web tab, add these environment variables:
      - `DJANGO_SETTINGS_MODULE`: `nirdhar_project.settings_production`
      - `SECRET_KEY`: `your-secure-secret-key`

13. **Secure the SECRET_KEY**:
    - Generate a new secure secret key:
      ```
      python -c "import secrets; print(secrets.token_urlsafe(50))"
      ```
    - Add it to your environment variables

14. **Reload the web app** and visit your site at yourusername.pythonanywhere.com

## Troubleshooting

- Check the error logs in the Web tab
- Make sure all paths in the WSGI file match your actual directory structure
- Verify that your virtual environment has all the required packages
- Check that static files are correctly configured

## Updates and Maintenance

To update your site after making changes to the repository:

1. Pull the latest changes:
   ```
   cd ~/nirdhar-backend
   git pull
   
   # Update the website repository too
   cd website
   git pull
   cd ..
   ```

2. Collect static files and run migrations:
   ```
   python manage.py collectstatic --noinput
   python manage.py migrate
   ```

3. Reload the web app from the Web tab 