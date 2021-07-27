"""
Django settings for ExtraHour project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v(3p09$t^l_et$v-2ifymh+nnkzc2m(x*t$tx#@rej4yeca%(u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.1.5','127.0.0.1',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'six',
    'accounts',
    'freelancer',
    'client',
    'job',
    'purposal_contract',
    'blog',
    #  'nested_admin',
     'django_extensions',
     'skill_test',
     'rest_framework',
     'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ExtraHour.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'ExtraHour/templates')],
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

WSGI_APPLICATION = 'ExtraHour.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ExtraHour',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost'

    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/karachi'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STRIPE_PUBLISHABLE_KEY = 'pk_test_51HvfRyCmPgXictcT8JQF2l1yDJXakV8rh8UaepjMJXEWl32ZP8Hd0xUTTQTzL5lXN8Ha3uKpiLN4SVXJduRfz4sf00wd5a4GVd'
STRIPE_SECRET_KEY = 'sk_test_51HvfRyCmPgXictcTGNI4iZFDPNmaSL8lWcGJ2FvfUi4DfvpLGxfqmpZI8RZ9vx4XK64CDQrCCi2IpyZFjgPRiqti00yOW1HFVI'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'stic')]
STATIC_ROOT = os.path.join(BASE_DIR , 'assets')

MEDIA_ROOT = os.path.join (BASE_DIR, 'assets/images')
MEDIA_URL = '/image/'
#sending email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'usmanaftababbasi420@gmail.com'
EMAIL_HOST_PASSWORD = 'Hydrogen302'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
LOGIN_REDIRECT_URL = '/'

APPEND_SLASH=False
GRAPH_MODELS ={
    'all_application': True,
    'group_models':True,
}