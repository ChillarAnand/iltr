import os


SITE_URL = os.environ.get('SITE_URL', '').rstrip('/')

ADMINS = (
    ('anand', 'anand21nanda@gmail.com'),
)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# SECRET_KEY = os.environ.get('SECRET_KEY', None)
SECRET_KEY = '6sd983****************LKSDF'

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE', None),
        'NAME': os.environ.get('DB_NAME', None),
        'USER': os.environ.get('DB_USER', None),
        'PASSWORD': os.environ.get('DB_PASSWORD', None),
        'HOST': os.environ.get('DB_HOST', None),
        'PORT': os.environ.get('DB_PORT', None)
    }
}

# DEBUG = os.environ.get('DEBUG', False)
DEBUG = True

TEMPLATE_DEBUG = DEBUG


STATIC_URL = '/static/'

ALLOWED_HOSTS = []


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.auth',

    'apps.books',
    'django_extensions',
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'iltr.urls'

WSGI_APPLICATION = 'iltr.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# email settings
EMAIL_USE_TLS = False
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'nandapk0@gmail.com'
EMAIL_HOST_PASSWORD = 'f33lg00d'
