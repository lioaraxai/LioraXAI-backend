"""
WSGI config for PythonAnywhere deployment.

This file contains the WSGI application used by PythonAnywhere.
Copy this file to the path specified in your PythonAnywhere configuration.
"""

import os
import sys

# Path to your code
path = '/home/your_username/lioraxai'
if path not in sys.path:
    sys.path.append(path)

# The environment variable to set to 'production'
os.environ['DJANGO_SETTINGS_MODULE'] = 'lioraxai_project.settings_production'

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

application = StaticFilesHandler(get_wsgi_application()) 