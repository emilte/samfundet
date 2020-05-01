import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


HEROKU = os.environ.get('HEROKU')

DEBUG = False
ALLOWED_HOSTS = []

LOGIN_REDIRECT_URL = 'accounts:profile'
LOGIN_URL = 'accounts:login'
LOGOUT_REDIRECT_URL = 'accounts:login'

# Static
STATIC_ROOT = os.path.join(BASE_DIR, 'staticroot')
STATIC_URL = '/static/'

# Media
MEDIA_ROOT = os.path.join(BASE_DIR, "mediaroot")
MEDIA_URL = '/media/'

# Custom User model
AUTH_USER_MODEL = 'accounts.User'

# Production settings:
SECURE_HSTS_SECONDS = 60 # TODO: Find a decent value
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = "DENY"


DATE_INPUT_FORMATS = [
    '%d-%m-%Y',
    '%d.%m.%Y',
    '%d/%m/%Y',
]


# Application definition
INSTALLED_APPS = [
    'accounts',
    'main',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'blog',
    'events',
    'recruitment',
    'info',

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

ROOT_URLCONF = 'main.urls'

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

WSGI_APPLICATION = 'main.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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


LANGUAGE_CODE = 'nb'

TIME_ZONE = 'Europe/Oslo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Custom settings that overwrite this.
try:
    from .local_settings import *
    print("== IMPORTED: local_settings ==")
except:
    print("== local_settings was not imported ==")

if HEROKU:
    try:
        from .heroku_settings import *
        print("== IMPORTED: heroku_settings ==")
    except:
        print("== heroku_settings was not imported ==")
else:
    try:
        from .dev_settings import *
        print("== IMPORTED: dev_settings ==")
    except:
        print("== dev_settings was not imported ==")
