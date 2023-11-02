from django.core.cache import cache


def ads_caching(model):
    model_name = model._meta.verbose_name.lower()
    ads_queryset = model.objects.five_low_score_ads()
    ads_list = [ads for ads in ads_queryset]
    cache.set(model_name, ads_list, timeout=None)
