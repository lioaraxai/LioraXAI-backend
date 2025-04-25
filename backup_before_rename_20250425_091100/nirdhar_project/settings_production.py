"""
Production settings for nirdhar_project.

These settings override the default settings for production deployment.
"""

from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Add your PythonAnywhere domain to allowed hosts
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com', 'www.yourdomain.com']  # Replace with your actual domains

# Configure the static file serving
STATIC_ROOT = '/home/yourusername/nirdhar-backend/staticfiles'  # Replace 'yourusername'

# HTTPS settings
SECURE_SSL_REDIRECT = True  # Redirect HTTP to HTTPS
SESSION_COOKIE_SECURE = True  # Set secure flag on session cookies
CSRF_COOKIE_SECURE = True  # Set secure flag on CSRF cookies
SECURE_BROWSER_XSS_FILTER = True  # Enable browser XSS filtering
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent MIME type sniffing
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')  # Needed for proxy servers

# Email settings for production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yourmailprovider.com'  # Replace with your mail provider
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@yourdomain.com'  # Replace with your email
EMAIL_HOST_PASSWORD = 'your-email-password'  # Replace with your email password
DEFAULT_FROM_EMAIL = 'Nirdhar <your-email@yourdomain.com>' 