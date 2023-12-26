import os

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

CSRF_TRUSTED_ORIGINS = ["https://ads-api.gozle.com.tm", "http://172.16.1.224:7577"]
ALLOWED_HOSTS = ["ads-api.gozle.com.tm", "127.0.0.1", "172.16.1.224"]

# Cache
REDIS_USERNAME = os.getenv("REDIS_USERNAME")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_KEY_PREFIX = os.getenv("REDIS_KEY_PREFIX")

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
#        "LOCATION": f"redis://{REDIS_USERNAME}:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/",
#        "KEY_PREFIX": f"{REDIS_KEY_PREFIX}",
#        'OPTIONS': {
#            'CLIENT_CLASS': 'helpers.custom_redis_cluster.CustomRedisCluster',
#        }
    }
}


# Celery
CELERY_BROKER_URL = f"redis://127.0.0.1:6379/"


# Security
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True
