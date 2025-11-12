"""
Development settings for running the project locally.

Usage:
  - Export DJANGO_SETTINGS_MODULE=enginer.devsettings, or
  - Run management commands with:  python manage.py runserver --settings=enginer.devsettings

This file imports all defaults from the base settings and overrides
production-leaning options to be friendlier for local development.
"""

from .settings import *  # noqa

# Core dev flags
DEBUG = True
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]

# Cookies: allow HTTP in dev
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# Email: print emails to console in dev
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_USE_TLS = False
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

# Third-party integrations: set safe dev defaults
AMADEUS_CLIENT_ID = 'dummy'
AMADEUS_CLIENT_SECRET = 'dummy'
GOOGLE_MAPS_API_KEY = 'dummy'

# reCAPTCHA: use public test keys in dev
# These are official Google reCAPTCHA v3 test keys.
RECAPTCHA_PUBLIC_KEY = '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI'
RECAPTCHA_PRIVATE_KEY = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'
RECAPTCHA_DEFAULT_ACTION = 'generic'
RECAPTCHA_SCORE_THRESHOLD = 0.5

# Optional: relax CSP a bit for dev if needed (kept as in base for now)
# CONTENT_SECURITY_POLICY = CONTENT_SECURITY_POLICY
