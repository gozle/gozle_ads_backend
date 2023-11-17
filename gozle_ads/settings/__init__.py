import os

from dotenv import load_dotenv

# dotenv config
load_dotenv()

environ = os.environ.get("DJANGO_SETTINGS", "local")

if environ.endswith("local"):
    from .local import *
else:
    from .production import *
