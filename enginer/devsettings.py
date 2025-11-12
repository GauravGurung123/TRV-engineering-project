"""
Development settings for running the project locally.

Usage:
  - Export DJANGO_SETTINGS_MODULE=enginer.devsettings, or
  - Run management commands with:  python manage.py runserver --settings=enginer.devsettings

This file imports all defaults from the base settings and overrides
production-leaning options to be friendlier for local development.
"""

from .settings import *  # noqa
import copy

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
# RECAPTCHA_PUBLIC_KEY = '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI'
# RECAPTCHA_PRIVATE_KEY = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'
# RECAPTCHA_DEFAULT_ACTION = 'generic'
# RECAPTCHA_SCORE_THRESHOLD = 0.5

# reCAPTCHA v3 Configuration
RECAPTCHA_PUBLIC_KEY = 'test-key'  # Replace with your v3 site key
RECAPTCHA_PRIVATE_KEY = 'test-key'  # Replace with your v3 secret key
RECAPTCHA_DEFAULT_ACTION = 'login'  # Or 'generic' if used in multiple places
RECAPTCHA_SCORE_THRESHOLD = 0.5  # Adjust threshold as needed (0.0 to 1.0)
RECAPTCHA_REQUIRED_SCORE = 0.5  # Same as threshold
RECAPTCHA_VERIFY_REQUEST_TIMEOUT = 10  # seconds

# Optional: relax CSP a bit for dev if needed (kept as in base for now)
# Allow unpkg.com for scripts and styles in development so CDN assets like
# htmx, hyperscript, and swiper can load without CSP violations.
# Production CSP remains strict as defined in base settings.
try:
    _base_csp = copy.deepcopy(CONTENT_SECURITY_POLICY)
    _directives = _base_csp.get("DIRECTIVES", {})

    def _extend(dir_name, *values):
        current = tuple(_directives.get(dir_name, tuple()))
        # Keep order stable and avoid duplicates
        new = list(current)
        for v in values:
            if v not in new:
                new.append(v)
        _directives[dir_name] = tuple(new)

    # Needed for <script src="https://unpkg.com/...">
    _extend("script-src", "https://unpkg.com")
    # Needed for <link rel="stylesheet" href="https://unpkg.com/...">
    _extend("style-src", "https://unpkg.com")
    # Allow Google Maps JavaScript API in development
    _extend("script-src", "https://maps.googleapis.com")
    _extend("connect-src", "https://maps.googleapis.com")

    CONTENT_SECURITY_POLICY = {
        "DIRECTIVES": _directives
    }
except Exception:
    # If base CSP is missing for any reason, define a permissive dev CSP fallback
    CONTENT_SECURITY_POLICY = {
        "DIRECTIVES": {
            "default-src": ("'self'",),
            "script-src": ("'self'", "https://unpkg.com"),
            "style-src": ("'self'", "https://fonts.googleapis.com", "https://unpkg.com"),
            "font-src": ("'self'", "https://fonts.gstatic.com"),
            "img-src": ("'self'", "data:"),
            "frame-ancestors": ("'none'",),
            "form-action": ("'self'",),
            "object-src": ("'none'",),
        }
    }
