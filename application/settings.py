"""
settings.py

Configuration for Flask app

Important: Place your keys in the secret_keys.py module, 
           which should be kept out of version control.

"""

import os

from secret_keys import CSRF_SECRET_KEY, SESSION_KEY


DEBUG_MODE = False
CACHE_ENABLED = True

# Auto-set debug mode based on App Engine dev environ
if 'SERVER_SOFTWARE' in os.environ and os.environ['SERVER_SOFTWARE'].startswith('Dev'):
    DEBUG_MODE = True
    CACHE_ENABLED = False

DEBUG = PROFILER_ENABLED = DEBUG_MODE

# Set secret keys for CSRF protection
SECRET_KEY = CSRF_SECRET_KEY
CSRF_SESSION_KEY = SESSION_KEY

CSRF_ENABLED = True


CACHE_TIMEOUT = 60*60*24