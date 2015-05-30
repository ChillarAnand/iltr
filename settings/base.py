import os


SITE_URL = os.environ.get('SITE_URL', '').rstrip('/')

ADMINS = (
    ('anand', 'anand21nanda@gmail.com'),
)

BASE_DIR = os.path.dirname(__file__)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_URL = '/static/'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.auth',

    'apps.books',
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
