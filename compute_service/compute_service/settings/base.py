from os import environ
from os.path import join, abspath, dirname

import djcelery

from django.core.exceptions import ImproperlyConfigured


here = lambda *x: join(abspath(dirname(__file__)), *x)
PROJECT_ROOT = here("..", "..")
root = lambda *x: join(abspath(PROJECT_ROOT), *x)

def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)


DEBUG = False
TEMPLATE_DEBUG = DEBUG

BASE_URL = 'http://%s' % get_env_variable('TB_HOST')

ADMINS = (
    (get_env_variable('TB_ADMIN_NAME'), get_env_variable('TB_ADMIN_EMAIL')),
)

DEFAULT_FROM_EMAIL = '%s <%s>' % ADMINS[0]

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable('TB_DB_NAME'),
        'USER': get_env_variable('TB_DB_USER'),
        'PASSWORD': get_env_variable('TB_DB_PASSWORD'),
        'HOST': get_env_variable('TB_DB_HOST'),
        'PORT': get_env_variable('TB_DB_PORT'),
    }
}

ALLOWED_HOSTS = [get_env_variable('TB_HOST')]

TIME_ZONE = get_env_variable('TB_TIME_ZONE')

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = root("results")

MEDIA_URL = '/results/'

STATIC_ROOT = root("static")

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    root("assets"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = get_env_variable('TB_SECRET_KEY')

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

CORS_ORIGIN_WHITELIST = (
    'mechanicsacademy.com',
)

ROOT_URLCONF = 'compute_service.urls'

WSGI_APPLICATION = 'compute_service.wsgi.application'

TEMPLATE_DIRS = (
    root("templates"),
)

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

THIRD_PARTY_APPS = (
    'south',
    'rest_framework',
    'rest_framework.authtoken',
    'djcelery',
    'corsheaders'
)

djcelery.setup_loader()

LOCAL_APPS = (
    'jobs',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

REST_FRAMEWORK = {
    'PAGINATE_BY': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
