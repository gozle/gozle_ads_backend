from django.contrib import admin

from .models import Banner, Device, Imput, Video


class AdsAdmin(admin.ModelAdmin):
    exclude = ("published_at", "deleted_at")

admin.site.register(Banner, AdsAdmin)
admin.site.register(Device)
admin.site.register(Imput, AdsAdmin)
admin.site.register(Video, AdsAdmin)
