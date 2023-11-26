from django.db import models
from django.utils.translation import gettext_lazy as _


class Province(models.Model):
    name = models.CharField(max_length=10)
    code_name = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return f"{self.code_name} | {self.name}"


class City(models.Model):
    name = models.CharField(max_length=15)
    code_name = models.CharField(max_length=3, unique=True)
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
        related_name="cities"
    )

    def __str__(self):
        return f"{self.code_name} | {self.name}"
    

    class Meta:
        verbose_name_plural = "cities"
