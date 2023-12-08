from django.db import models
from django.utils.translation import gettext_lazy as _
from slugify import slugify


class Province(models.Model):
    name = models.CharField(max_length=10, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id}. {self.name}"


class City(models.Model):
    name = models.CharField(max_length=15, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
        related_name="cities"
    )

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id}. {self.name}"
    

    class Meta:
        verbose_name_plural = "cities"
