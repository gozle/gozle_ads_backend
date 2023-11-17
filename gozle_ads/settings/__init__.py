import os

from django.conf import settings

from dotenv import load_dotenv

root_urlconf = settings.ROOT_URLCONF

# dotenv config

from .base import BASE_DIR
dotenv_path = f"{BASE_DIR}/dist.env"
load_dotenv(dotenv_path)

environ = os.environ.get("DJANGO_SETTINGS", "local")

if environ.endswith("local"):
    from .local import *
else:
    from .production import *
