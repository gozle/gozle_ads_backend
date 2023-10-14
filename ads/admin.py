from django.contrib import admin

from .models import (
    Banner,
    Imput,
    Video,
    Device
)

admin.site.register(Banner)
admin.site.register(Device)
admin.site.register(Imput)
admin.site.register(Video)
