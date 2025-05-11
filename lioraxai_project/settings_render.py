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

# Add Jazzmin settings for better admin UI
JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "LioraXAI Admin",
    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "LioraXAI",
    # Logo to use for your site, must be present in static files
    "site_logo": None,
    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",
    # Welcome text on the login screen
    "welcome_sign": "Welcome to LioraXAI Admin",
    # Copyright on the footer
    "copyright": "LioraXAI Ltd",
    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "auth.User",
    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,
    # List of apps (and/or models) to base side menu ordering off of
    "order_with_respect_to": ["auth", "lioraxai_app"],
    # Custom icons for side menu apps/models
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "lioraxai_app.Contact": "fas fa-address-book",
        "lioraxai_app.DemoRequest": "fas fa-clipboard-list",
        "lioraxai_app.Subscriber": "fas fa-envelope",
    },
    # Theme UI customizations
    "show_ui_builder": True,
    "changeform_format": "horizontal_tabs",
    "custom_css": "css/admin_custom.css",
    "custom_js": None,
    # Theme
    "dark_mode_theme": "darkly",
}

# Additional Jazzmin settings
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-indigo",
    "accent": "accent-indigo",
    "navbar": "navbar-indigo navbar-dark",
    "no_navbar_border": True,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-indigo",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "cyborg",
    "dark_mode_theme": "cyborg",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}

# Override SECRET_KEY in production
if 'SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ['SECRET_KEY'] 