"""
Django settings for KNN project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rh87(0_ed1^!%slec7ug!eafc)l_c6yeg*e6&gp&5h@nl@s8t2'

# SECURITY WARNING: don't run with debug turned on in production!
# settings.py
DEBUG = True
ALLOWED_HOSTS = ['*']

# # Error handlers
# handler404 = 'path.to.your.views.error'



# Application definition

INSTALLED_APPS = [
  'modeltranslation',
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'django.contrib.sites',
  "core",
  'raport',
  'ckeditor',
  'api',
  'social_django',
  'baseuser.apps.BaseuserConfig',
  'rosetta',
  'rest_framework',
  'rest_framework_simplejwt',
  'django_celery_beat',
  
]
SITE_ID = 1

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.locale.LocaleMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',


]

REST_FRAMEWORK = {
    
    'DEFAULT_AUTHENTICATION_CLASSES': (

        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
    
}
SESSION_COOKIE_AGE = 100000


CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Baku'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'kenansdq@gmail.com'
EMAIL_HOST_PASSWORD = 'e i s m r c u f q x j z y y e f'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


SESSION_EXPIRE_AT_BROWSER_CLOSE = False

ROOT_URLCONF = 'KNN.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
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

WSGI_APPLICATION = 'KNN.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# change to postgresql
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'KNN',
    'USER': 'KNN',
    'PASSWORD': 'KNN',
    'PORT': 5432,
    'HOST': 'localhost',
  }
}
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/
MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
LANGUAGE_CODE = 'en'
LANGUAGES = (
  ("en", _("English")),
  ("az", _("Azerbaijani")),
  ("tr", _("Turkish")),
)

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'

MODELTRANSLATION_LANGUAGES = ("en", "az", "tr")

TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "docs"),
    '/home/sadiq/Documents/Hospital-Project/hospital/staticfiles/',
]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'baseuser.BaseUser'

AUTHENTICATION_BACKENDS = (
  'social_core.backends.google.GoogleOAuth2',
  'django.contrib.auth.backends.ModelBackend',
  'social_core.backends.facebook.FacebookOAuth2',
)
SOCIAL_AUTH_FACEBOOK_KEY = "283640947654507"
SOCIAL_AUTH_FACEBOOK_SECRET = "fff4f0fca0473c2734211684005a08c0"
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '361863753250-aadskm56r0ckegbnu1jtgd3h35kpid8t.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [
  ('name', 'name'),
  ('email', 'email'),
  ('picture', 'picture'),
  ('link', 'profile_url'),
]

# LOGIN_URL = ''
# LOGIN_URL = '/auth/login/google-oauth2/'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
SOCIAL_AUTH_URL_NAMESPACE = 'social'

HAYSTACK_CONNECTIONS = {
  'default': {
    'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
    'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
  },
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = '/home/sadiq/Documents/Hospital-Project/hospital/static/'


ALLOWED_HOSTS = ['sadiqmustafayev.github.io','127.0.0.1', 'localhost']
