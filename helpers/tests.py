from datetime import timedelta

from ads.models import Banner, Imput


def banner_model(
    text: str = "Gozle Portal",
    description: str = "Market where you can buy computer games and apps",
    link: str = "https://store.gozle.com.tm/",
    age_from: int = 12,
    age_to: int = 18,
    duration: int = timedelta(days=1),
    **kwargs
):
    banner = Banner(
        text=text, description=description, link=link, age_from=age_from, age_to=age_to, duration=duration
    )

    return banner


def create_banner(
    text: str = "Gozle Portal",
    description: str = "Market where you can buy computer games and apps",
    link: str = "https://store.gozle.com.tm/",
    age_from: int = 12,
    duration: int = timedelta(days=1),
    **kwargs
):
    banner = Banner.objects.create(
        text=text, description=description, link=link, age_from=age_from, duration=duration
    )

    return banner


def create_imput(
    link: str = "https://store.gozle.com.tm/",
    duration: int = timedelta(days=1),
    **kwargs
):
    imput = Imput.objects.create(link=link, duration=duration)

    return imput
