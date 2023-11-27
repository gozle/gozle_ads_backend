from django.contrib import admin
from django.utils import timezone
from datetime import timedelta

from .models import Banner, Device, Imput, Video


class AdsAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change) -> None:
        starts_at = obj.starts_at
        now = timezone.now() + timedelta(seconds=5)
        if now >= starts_at:
            obj.set_as_active()

        return super().save_model(request, obj, form, change)

    exclude = ("published_at", "deleted_at")


admin.site.register(Banner, AdsAdmin)
admin.site.register(Device)
admin.site.register(Imput, AdsAdmin)
admin.site.register(Video, AdsAdmin)
