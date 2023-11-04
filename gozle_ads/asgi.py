"""
ASGI config for gozle_ads project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from django.urls import re_path

from channels.routing import ProtocolTypeRouter, URLRouter

from ads.consumers import BannerConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gozle_ads.settings')

ws_patterns = [
    re_path(r"ws/banner/", BannerConsumer.as_asgi())
]


application = ProtocolTypeRouter({
        "http": get_asgi_application(),
        "websocket": URLRouter(ws_patterns),
})
