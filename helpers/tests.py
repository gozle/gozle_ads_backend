from typing import Any, Tuple

from ads.models import Banner, Imput
from devices.models import Device


def banner_model(
    text: str = "Gozle Portal",
    description: str = "Market where you can buy computer games and apps",
    link: str = "https://store.gozle.com.tm/",
    age_from: int = 12,
    age_to: int = 18,
    **kwargs
):
    banner = Banner(
        text=text, description=description, link=link, age_from=age_from, age_to=age_to
    )

    return banner


def create_banner(
    text: str = "Gozle Portal",
    description: str = "Market where you can buy computer games and apps",
    link: str = "https://store.gozle.com.tm/",
    age_from: int = 12,
    **kwargs
):
    banner = Banner.objects.create(
        text=text, description=description, link=link, age_from=age_from
    )

    return banner


def create_imput(
    link: str = "https://store.gozle.com.tm/",
    **kwargs
):
    imput = Imput.objects.create(link=link)

    return imput
