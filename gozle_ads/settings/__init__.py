import os

environ = os.environ.get("DJANGO_SETTINGS", "local")

if environ.endswith("local"):
    from .local import *
else:
    from .production import *
