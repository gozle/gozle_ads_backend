from django.db import models
from django.utils.translation import gettext_lazy as _


class Province(models.Model):
    name = models.CharField(max_length=10)
    code_name = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.code_name} | {self.name}"
