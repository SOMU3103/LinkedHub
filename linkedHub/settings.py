"""
Django settings for linkedHub project — LOCAL DEVELOPMENT ONLY
"""

from pathlib import Path
import os
from django.contrib.messages import constants as messages
from decouple import config, Csv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ─────────────────────────────────────────────────────────────────────────────
# SECURITY — relaxed for local dev
# ─────────────────────────────────────────────────────────────────────────────
SECRET_KEY = config('SECRET_KEY', default='django-insecure-local-dev-secret-key-change-in-prod')

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

SECURE_BROWSER_XSS_FILTER    = False
SECURE_CONTENT_TYPE_NOSNIFF  = False
SECURE_SSL_REDIRECT          = False
SESSION_COOKIE_SECURE        = False
CSRF_COOKIE_SECURE           = False

# ─────────────────────────────────────────────────────────────────────────────
# PASSWORD HASHING
# ─────────────────────────────────────────────────────────────────────────────
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

# ─────────────────────────────────────────────────────────────────────────────
# INSTALLED APPS
# ─────────────────────────────────────────────────────────────────────────────
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # Django OTP
    'django_otp',
    'django_otp.plugins.otp_email',
    # Third-party
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    # Local apps
    'shop',
    # NOTE: 'storages' removed — not needed for local dev (no S3)
]

# ─────────────────────────────────────────────────────────────────────────────
# MIDDLEWARE
# ─────────────────────────────────────────────────────────────────────────────
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'linkedHub.urls'

# ─────────────────────────────────────────────────────────────────────────────
# TEMPLATES
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
}]

WSGI_APPLICATION = 'linkedHub.wsgi.application'

# ─────────────────────────────────────────────────────────────────────────────
# DATABASE — local PostgreSQL
# ─────────────────────────────────────────────────────────────────────────────
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql',
        'NAME':     config('DB_NAME',     default='linkedhub'),
        'USER':     config('DB_USER',     default='postgres'),
        'PASSWORD': config('DB_PASSWORD', default=''),
        'HOST':     config('DB_HOST',     default='127.0.0.1'),
        'PORT':     config('DB_PORT',     default='5432'),
    }
}

# ─────────────────────────────────────────────────────────────────────────────
# PASSWORD VALIDATION
# ─────────────────────────────────────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ─────────────────────────────────────────────────────────────────────────────
# INTERNATIONALISATION
# ─────────────────────────────────────────────────────────────────────────────
LANGUAGE_CODE = 'en-us'
TIME_ZONE     = 'UTC'
USE_I18N      = True
USE_TZ        = True

# ─────────────────────────────────────────────────────────────────────────────
# STATIC FILES  (served by WhiteNoise in local dev too)
# ─────────────────────────────────────────────────────────────────────────────
STATIC_URL  = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# ─────────────────────────────────────────────────────────────────────────────
# MEDIA FILES — local filesystem (replaces S3 for local dev)
# ─────────────────────────────────────────────────────────────────────────────
MEDIA_URL  = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ─────────────────────────────────────────────────────────────────────────────
# STORAGE — plain defaults; no S3 / storages package needed locally
# ─────────────────────────────────────────────────────────────────────────────
STORAGES = {
    "default": {                          # media uploads → local disk
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {                      # static files → WhiteNoise
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

# WhiteNoise — sensible dev settings
WHITENOISE_MANIFEST_STRICT = False
WHITENOISE_AUTOREFRESH     = True   # pick up changed static files immediately
WHITENOISE_MAX_AGE         = 0      # no browser caching during development

# ─────────────────────────────────────────────────────────────────────────────
# DEFAULT PRIMARY KEY
# ─────────────────────────────────────────────────────────────────────────────
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ─────────────────────────────────────────────────────────────────────────────
# CUSTOM USER MODEL
# ─────────────────────────────────────────────────────────────────────────────
AUTH_USER_MODEL = 'shop.CustomUser'

# ─────────────────────────────────────────────────────────────────────────────
# AUTHENTICATION
# ─────────────────────────────────────────────────────────────────────────────
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1  # Use 1 for local development (make sure django.contrib.sites is migrated)

LOGIN_URL           = '/accounts/login/'
LOGIN_REDIRECT_URL  = 'send_otp'
LOGOUT_REDIRECT_URL = '/accounts/login/'

# ─────────────────────────────────────────────────────────────────────────────
# ALLAUTH
# ─────────────────────────────────────────────────────────────────────────────
ACCOUNT_AUTHENTICATION_METHOD      = 'email'
ACCOUNT_EMAIL_REQUIRED             = True
ACCOUNT_USERNAME_REQUIRED          = True
ACCOUNT_EMAIL_VERIFICATION         = 'mandatory'
ACCOUNT_LOGOUT_ON_GET              = True
ACCOUNT_SESSION_REMEMBER           = True
ACCOUNT_USERNAME_MIN_LENGTH        = 3
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7

ACCOUNT_RATE_LIMITS = {
    'login_failed': '5/5m',
}

ACCOUNT_FORMS = {
    'signup': 'shop.forms.CustomSignupForm',
}

# Social account
SOCIALACCOUNT_AUTO_SIGNUP       = True
SOCIALACCOUNT_EMAIL_REQUIRED    = True
SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'
SOCIALACCOUNT_QUERY_EMAIL       = True

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'OAUTH_PKCE_ENABLED': True,
    }
}

# ─────────────────────────────────────────────────────────────────────────────
# MESSAGES
# ─────────────────────────────────────────────────────────────────────────────
MESSAGE_TAGS = {
    messages.DEBUG:   'secondary',
    messages.INFO:    'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR:   'danger',
}

# ─────────────────────────────────────────────────────────────────────────────
# EMAIL — console backend for local dev (prints emails to terminal)
# ─────────────────────────────────────────────────────────────────────────────
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# To test with a real SMTP server instead, set these in your .env and switch
# EMAIL_BACKEND to 'django.core.mail.backends.smtp.EmailBackend':
#   EMAIL_HOST, EMAIL_PORT, EMAIL_USE_TLS, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD

OTP_EMAIL_SENDER  = config('EMAIL_HOST_USER', default='dev@localhost')
OTP_EMAIL_SUBJECT = 'Your OTP Code'

# ─────────────────────────────────────────────────────────────────────────────
# OTP
# ─────────────────────────────────────────────────────────────────────────────
OTP_LOGIN_URL = '/send-otp/'

# ─────────────────────────────────────────────────────────────────────────────
# LOGGING
# ─────────────────────────────────────────────────────────────────────────────
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
    'loggers': {
        'django.db.backends': {
            'level': 'INFO',           # set to DEBUG to see every SQL query
            'handlers': ['console'],
            'propagate': False,
        },
    },
}