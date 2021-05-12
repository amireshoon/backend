"""
Django settings for ratecompany project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static/media')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    # second party
    'rest_framework',
    'rest_framework_swagger',
    'corsheaders',
    'location_field.apps.DefaultConfig',  # https://github.com/caioariede/django-location-field
    # our
    'authnz',
    'config',
    'company',
    'donate',
    'job',
    'review',
    'question',
    'utilities',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'utilities.responses.ExceptionHandlerMiddleware',

]

ROOT_URLCONF = 'ratecompany.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '../../templates')]
        ,
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

WSGI_APPLICATION = 'ratecompany.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/
from django.utils.translation import ugettext_lazy as _
LOCALE_PATHS = (
    os.path.join(os.path.dirname(BASE_DIR), 'locale'),
)

LANGUAGES = (
    ('fa', _('Persian')),
    ('en', _('English')),
)

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

JWT_AUTH = {
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=30),
    'JWT_ALLOW_REFRESH': True,
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'utilities.utilities.jwt_response_payload_handler',
    'JWT_GET_USER_SECRET_KEY': 'utilities.utilities.jwt_get_secret_key',
}

SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'SHOW_REQUEST_HEADERS': True,
    'SECURITY_DEFINITIONS': {
        'apiKey': {
            'type': 'apiKey',
            'description': 'Personal API Key authorization',
            'name': 'Authorization',
            'in': 'header',
        },
    },
}

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': '10/day'
    }
    # 'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.AcceptHeaderVersioning',
    # 'DEFAULT_VERSION': '2.0',
    # 'VERSION_PARAM': 'version',
    # 'ALLOWED_VERSIONS': ('2.0', ),
    # 'EXCEPTION_HANDLER': 'api.tools.exception_handler'
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        # 'LOCATION': '/var/run/redis/redis.sock',  # over sock
        'LOCATION': 'redis://localhost:6379/0',  # over http
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
    }
}


# CORS https://github.com/ottoyiu/django-cors-headers

# CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
    'localhost:3000',
    'localhost:3001',
    'localhost:3002',
    'https://jobguy.work',
    'jobguy.work',
    'hr.jobguy.work',
    'http://hr.jobguy.work',
    'https://hr.jobguy.work',
    'develop.jobguy.work',
    'https://develop.jobguy.work',
)

APPEND_SLASH = True

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY', None)

if not SOCIAL_AUTH_GOOGLE_OAUTH2_KEY:
    raise Exception('Add SOCIAL_AUTH_GOOGLE_OAUTH2_KEY env variable')

SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET', None)

if not SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET:
    raise Exception('Add SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET env variable')

LOCATION_FIELD = {
    'map.provider': 'openstreetmap',
    'map.zoom': 15,

    'search.provider': 'google',
    'search.suffix': '',

    # # Google
    # 'provider.google.api': '//maps.google.com/maps/api/js?sensor=false',
    # 'provider.google.api_key': '<INSERT GOOGLE API KEY>',
    # 'provider.google.api_libraries': '',
    # 'provider.google.map.type': 'ROADMAP',
    #
    # # Mapbox
    # 'provider.mapbox.access_token': '',
    # 'provider.mapbox.max_zoom': 18,
    # 'provider.mapbox.id': 'mapbox.streets',

    # OpenStreetMap
    'provider.openstreetmap.max_zoom': 16,

    # # misc
    # 'resources.root_path': LOCATION_FIELD_PATH,
    # 'resources.media': {
    #     'js': (
    #         LOCATION_FIELD_PATH + '/js/form.js',
    #     ),
    # },
}
