from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-a^kce@urmy@ey5uawx2v7hx*x!$^$%o-h7pve5kh!8)d=%i$1w'

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shop_backend_db',
        'USER': 'admin',
        'PASSWORD': '123456',
        'HOST':'localhost',
        'PORT': '5432'
    }
}

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

try:
    from .local_settings import *
except ImportError:
    from .prod_settings import *