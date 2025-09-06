"""
Django settings for eventpr project (adapted for Render / production).

- Reads sensitive values from environment variables.
- Uses WhiteNoise for static files.
- Supports DATABASE_URL (Postgres) with a sqlite fallback.
"""
import os
from pathlib import Path

import dj_database_url  # pip install dj-database-url
# NOTE: whitenoise is configured later (pip install whitenoise)

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY: read secret key & debug from environment
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'dev-secret-for-local-only')
DEBUG = os.environ.get('DJANGO_DEBUG', '') == '1'

# Hosts: provide a comma-separated string in env (e.g. "yourapp.onrender.com,localhost")
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost').split(',')

# Optionally set CSRF trusted origins (comma-separated), e.g. "https://yourapp.onrender.com"
_csrf_trusted = os.environ.get('DJANGO_CSRF_TRUSTED_ORIGINS')
if _csrf_trusted:
    CSRF_TRUSTED_ORIGINS = [x.strip() for x in _csrf_trusted.split(',')]

# Force Django to detect secure requests when behind a proxy (Render provides X-Forwarded-Proto)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Optional security toggles (enable in production by setting env var to "1")
SECURE_SSL_REDIRECT = os.environ.get('DJANGO_SECURE_SSL_REDIRECT', '') == '1'
SESSION_COOKIE_SECURE = os.environ.get('DJANGO_COOKIE_SECURE', '') == '1'
CSRF_COOKIE_SECURE = os.environ.get('DJANGO_COOKIE_SECURE', '') == '1'
# HSTS example (enable only when you fully trust your domain)
SECURE_HSTS_SECONDS = int(os.environ.get('DJANGO_HSTS_SECONDS', '0'))
SECURE_HSTS_INCLUDE_SUBDOMAINS = os.environ.get('DJANGO_HSTS_INCLUDE_SUBDOMAINS', '') == '1'
SECURE_HSTS_PRELOAD = os.environ.get('DJANGO_HSTS_PRELOAD', '') == '1'

# Application definition
INSTALLED_APPS = [
    'eventapp',
    'userapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # WhiteNoise middleware serves static files in production
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'eventpr.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # your templates folder (you used 'template' earlier)
        'DIRS': [os.path.join(BASE_DIR, 'template')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'eventpr.wsgi.application'

# Database: uses DATABASE_URL when provided, otherwise sqlite
DATABASES = {
    'default': dj_database_url.parse(
        os.environ.get('DATABASE_URL', f"sqlite:///{BASE_DIR / 'db.sqlite3'}"),
        conn_max_age=600
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = os.environ.get('DJANGO_TIME_ZONE', 'UTC')
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# In production collectstatic will copy these into STATIC_ROOT and WhiteNoise will serve them.
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Use WhiteNoise's compressed manifest storage for long-term caching in production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media (user uploaded files)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'pic'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication settings
LOGIN_URL = 'login'

# Simple logging to console (useful on Render to see stdout/stderr)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {'console': {'class': 'logging.StreamHandler',}},
    'root': {'handlers': ['console'], 'level': os.environ.get('DJANGO_LOG_LEVEL', 'INFO'),},
}
