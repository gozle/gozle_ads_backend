import os

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# REDIS CACHE

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": BROKER_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "KEY_PREFIX": "gozle_ads:"
        },
    }
}


CORS_ORIGIN_ALLOW_ALL = True


# Django Debug Toolbar
try:
    import debug_toolbar

    INSTALLED_APPS += ["debug_toolbar"]
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
    INTERNAL_IPS = [
        "127.0.0.1",
    ]
except ModuleNotFoundError:
    pass
