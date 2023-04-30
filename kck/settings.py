""" Django 3.2.4"""

from pathlib import Path
import psycopg2
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&0^_enc-c4l79p7d=g7p5_2nx4)&_s9v5vpux^m3!7&!ep!3ef'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['185.201.9.2', 'kckok.my', 'http://kckok.my', 'www.kckok.my', 'http://www.kckok.my', '.kckok.my', '*']


# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'kck2021',
    'tinymce',
    'django_summernote',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # Django Sitemap - installed app
    'django.contrib.sitemaps',
    'compressor',
]

# Define Site Id 
SITE_ID = 1

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

DEFAULT = {
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': [
    'advlist autolink link image lists charmap print preview hr anchor pagebreak',
    'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking',
    'table emoticons template paste help'
    ],
    'toolbar1': 'bold italic underline | alignleft aligncenter alignright alignjustify '
           '| bullist numlist | outdent indent | table | link image | codesample | preview code',
    'contextmenu': 'formats | link image',
    'menubar': False,
    'inline': False,
    'statusbar': True,
    'height': 360,
}

MIDDLEWARE = [
    # Compressor Starts
    'django.middleware.gzip.GZipMiddleware', 
    'htmlmin.middleware.HtmlMinifyMiddleware', 
    'htmlmin.middleware.MarkRequestMiddleware',
    # Compressor Ends
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kck.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'kck2021')],
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

WSGI_APPLICATION = 'kck.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'Delvin',
#        'USER': 'postgres',
#        'PASSWORD': 'admin',
#        'HOST': '127.0.0.1',
#        'PORT': '5432',
#    }
#}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'dbdjmfutnn3jep',
#       'USER': 'xtvbuaeepxmbyx',
#        'PASSWORD': '0dd65e237b5b214c1c098120af26f31724a4fbbb807561acdc8b45538ea42898',
#        'HOST': 'ec2-44-197-40-76.compute-1.amazonaws.com',
#        'PORT': 5432,
#    }
#}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ms'

TIME_ZONE = 'Asia/Singapore'

USE_I18N = False

USE_L10N = True

USE_TZ = True

from django.utils.translation import gettext as _

LANGUAGES = [
    ('en', _("English")),
]
LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale/"),
)

# Security
'''
SECURE_SSL_REDIRECT = False
SECURE_HSTS_PRELOAD = False
SECURE_HSTS_SECONDS = 31536000
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
'''

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
PROJECT_ROOT   =   os.path.join(os.path.abspath(__file__))

MEDIA_DIR = os.path.join(BASE_DIR,'media')
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'

STATIC_ROOT  =   os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

    # Compressor
    'compressor.finders.CompressorFinder',
)

# Minifying files
COMPRESS_ENABLED = not DEBUG
COMPRESS_CSS_HASHING_METHOD = 'content'
COMPRESS_FILTERS = {
    'css':[
        'compressor.filters.css_default.CssAbsoluteFilter',
        'compressor.filters.cssmin.rCSSMinFilter',
    ],
    'js':[
        'compressor.filters.jsmin.JSMinFilter',
    ]
}
HTML_MINIFY = True
KEEP_COMMENTS_ON_MINIFYING = True

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST="smtp.gmail.com"
EMAIL_POST=587
EMAIL_HOST_USER="kckokengineering@gmail.com"
EMAIL_HOST_PASSWORD="Kckokengineering1234"
EMAIL_USE_TLS=True