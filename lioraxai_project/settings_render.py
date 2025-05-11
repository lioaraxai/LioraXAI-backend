"""
Production settings for lioraxai_project deployment on Render.com

These settings override the default settings for production deployment.
"""

import os
import dj_database_url
from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Get the allowed hosts from environment variable or use default
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "lioraxai.onrender.com").split(",")

# Database configuration for Render
DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# Configure the static file serving
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# HTTPS settings
SECURE_SSL_REDIRECT = True  # Redirect HTTP to HTTPS
SESSION_COOKIE_SECURE = True  # Set secure flag on session cookies
CSRF_COOKIE_SECURE = True  # Set secure flag on CSRF cookies
SECURE_BROWSER_XSS_FILTER = True  # Enable browser XSS filtering
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent MIME type sniffing
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')  # Needed for proxy servers
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Email settings for production (Update with your email provider details)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.sendgrid.net')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587))
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'apikey')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'noreply@lioraxai.com')

# Override SECRET_KEY in production
if 'SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ['SECRET_KEY'] 