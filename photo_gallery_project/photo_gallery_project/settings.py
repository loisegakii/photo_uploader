from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------------------------------------
# SECURITY SETTINGS
# ------------------------------------------------------

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8fpo4(-&yx^e&rw^_5v+9l48w!%wq6h)k(3g0e4=4kyo)113m#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Hosts allowed to access the app
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# ------------------------------------------------------
# APPLICATIONS
# ------------------------------------------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your custom app
    'gallery',
]

# ------------------------------------------------------
# MIDDLEWARE
# ------------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ------------------------------------------------------
# TEMPLATES
# ------------------------------------------------------

ROOT_URLCONF = 'photo_gallery_project.urls'

TEMPLATES = [
    {
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
    },
]

WSGI_APPLICATION = 'photo_gallery_project.wsgi.application'

# ------------------------------------------------------
# DATABASE CONFIGURATION
# ------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'photo_gallery_db',
        'USER': 'loise',
        'PASSWORD': '7075',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# ------------------------------------------------------
# AUTHENTICATION SETTINGS
# ------------------------------------------------------

# Redirect to login page if not authenticated
LOGIN_URL = 'login'

# Redirect to this page after successful login
LOGIN_REDIRECT_URL = '/photos/'

# ------------------------------------------------------
# PASSWORD VALIDATION
# ------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ------------------------------------------------------
# INTERNATIONALIZATION
# ------------------------------------------------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ------------------------------------------------------
# STATIC AND MEDIA FILES
# ------------------------------------------------------

# Static files (CSS, JavaScript, etc.)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # Optional for dev

# Media files (user uploads like photos)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ------------------------------------------------------
# DEFAULT PRIMARY KEY TYPE
# ------------------------------------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
