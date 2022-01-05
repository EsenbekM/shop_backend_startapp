from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent



DEBUG = True



STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
