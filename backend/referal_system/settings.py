import os
from datetime import timedelta
from pathlib import Path
from string import ascii_letters, digits

from dotenv import load_dotenv

# from cryptography.fernet import Fernet


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-mshb*c824xuvaf6rg1==ebc8*%*=a+ft@ypu5dmz$qnz19^294"

SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "django-insecure-mshb*c824xuvaf6rg1==ebc8*%*=a+ft@ypu5dmz$qnz19^294",
)

DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost 127.0.0.1").split(" ")


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "rest_framework_simplejwt",
    "drf_spectacular",

    "api",
    "users",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "referal_system.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "referal_system.wsgi.application"


POSTGRES = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': os.getenv('POSTGRES_DB', 'django'),
    'USER': os.getenv('POSTGRES_USER', 'django'),
    'PASSWORD': os.getenv('POSTGRES_PASSWORD', ''),
    'HOST': os.getenv('DB_HOST', 'postgres'),
    'PORT': os.getenv('DB_PORT', 5432)
}

SQLITE3 = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite',
}

DB_ENGINE = (SQLITE3, POSTGRES)[os.getenv('DB_ENGINE_POSTGRES') == 'True']

DATABASES = {
    'default': DB_ENGINE
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Referal system API",
}

ONE_WEEK_IN_SECONDS = 604800

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(
        seconds=int(os.getenv("ACCESS_TOKEN_LIFETIME", ONE_WEEK_IN_SECONDS))
    ),
    "REFRESH_TOKEN_LIFETIME": timedelta(
        seconds=int(os.getenv("REFRESH_TOKEN_LIFETIME", ONE_WEEK_IN_SECONDS))
    ),
    'AUTH_HEADER_TYPES': ('Bearer',),
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "ROTATE_REFRESH_TOKENS": True,
}

AUTH_USER_MODEL = "users.User"

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

ONE_WEEK_IN_SECONDS = 604800

# CONSTANTS
MAX_LEN_USERNAME_USER_MODEL: int = 254
MAX_LEN_EMAIL_USER_MODEL: int = 254
MIN_LEN_PASSWORD_USER_MODEL: int = 8
MAX_LEN_PASSWORD_USER_MODEL: int = 30
MAX_LEN_HASH_PASSWORD_USER_MODEL: int = 128

# INVITE_CODE CONF
INVITE_CODE_CHARS = digits + ascii_letters
INVITE_CODE_LENGTH = 254

# CELERY

if os.getenv('DEV') == 'True':
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
else:
    CELERY_BROKER_URL = 'redis://redis:6379'
    CELERY_RESULT_BACKEND = 'redis://redis:6379'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"{CELERY_BROKER_URL}",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}


STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS  = os.path.join(BASE_DIR, 'static')


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"