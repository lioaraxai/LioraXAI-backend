"""
WSGI config for PythonAnywhere deployment.

This file contains the WSGI application used by PythonAnywhere.
Copy this file to the path specified in your PythonAnywhere configuration.
"""

import os
import sys

# Add the project directory to the sys.path
path = '/home/yourusername/nirdhar-backend'  # Replace 'yourusername' with your PythonAnywhere username
if path not in sys.path:
    sys.path.append(path)

# Set environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'nirdhar_project.settings'

# Import Django and the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application() 