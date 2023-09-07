"""
Django settings for NewsPortal project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os.path
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=-)#vmnkvkky0o#ci5d@rbnqme&#v=i=-#zacnbh0(vppnt9je'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'NewsPaper',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'django_apscheduler',

]

SITE_ID = 1

MIDDLEWARE = [
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'NewsPortal.urls'

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

WSGI_APPLICATION = 'NewsPortal.wsgi.application'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

LOGIN_REDIRECT_URL = "/news"

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "seirana.ramazanova"
EMAIL_HOST_PASSWORD = "htldkvryeovoyvtw"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = "seirana.ramazanova@yandex.ru"

SERVER_EMAIL = "seirana.ramazanova@yandex.ru"

CELERY_BROKER_URL = 'redis://default:YiGcMU9ExwJmCwDnwMcMkyKiRGr1ADel@redis-17212.c238.us-central1-2.gce.cloud.redislabs.com:17212'
CELERY_RESULT_BACKEND = 'redis://default:YiGcMU9ExwJmCwDnwMcMkyKiRGr1ADel@redis-17212.c238.us-central1-2.gce.cloud.redislabs.com:17212'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files')
    }}

ADMIN = []

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style' : '{',
    'formatters': {
        'simple': {
            'format': '{asctime} {levelname} {message}',
            'datefmt': '%Y. %m. %d %H:%M:%S',
            'style': '{'
        },
        'simple_module': {
            'format': '{asctime} {levelname} {message} {module}',
            'datefmt': '%Y. %m. %d %H:%M:%S',
            'style': '{'
        },
        'simple_path': {
            'format': '{asctime} {levelname} {message} {module} {pathname}',
            'datefmt': '%Y. %m. %d %H:%M:%S',
            'style': '{'
        },
        'simple_exc': {
            'format': '{asctime} {levelname} {message} {module} {pathname} {exc_info}',
            'datefmt': '%Y. %m. %d %H:%M:%S',
            'style': '{'
        }
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console_debug': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple_path'
        },
        'console_error': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple_exc'
             },
        'file_info': {
            'class': 'logging.FileHandler',
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'filename': 'general.log',
            'formatter': 'simple_module'
        },
        'file_error': {
            'class': 'logging.FileHandler',
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'filename': 'errors.log',
            'formatter': 'simple_exc'
        },
        'file_security': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'filename': 'security.log',
            'formatter': 'simple_module'
        },
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'formatter': 'simple_path'
        }

    },
    'loggers': {
        'django': {
            'handlers': ['console_debug', 'console_warning', 'console_error', 'file_info'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file_error', 'mail_admins'],
            'propagate': True

        },
        'django.server': {
            'handlers': ['file_error', 'mail_admins'],
            'propagate': True

        },
        'django.template': {
            'handlers': ['file_error'],
            'propagate': True

        },
        'django.db.backends': {
            'handlers': ['file_error'],
            'propagate': True

        },
        'django.security': {
            'handlers': ['file_security'],
            'propagate': True
        }
    }
}


