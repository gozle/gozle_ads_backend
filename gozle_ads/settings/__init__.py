import os
from dotenv import load_dotenv

from .base import BASE_DIR

# dotenv config
dotenv_path = f"{BASE_DIR}/dist.env"
load_dotenv(dotenv_path)

environ = os.environ.get("DJANGO_SETTINGS", "local")

if environ.endswith("local"):
    from .local import *
else:
    from .production import *
