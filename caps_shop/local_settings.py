from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-a^kce@urmy@ey5uawx2v7hx*x!$^$%o-h7pve5kh!8)d=%i$1w'


DEBUG = True

ALLOWED_HOSTS = []

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

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')