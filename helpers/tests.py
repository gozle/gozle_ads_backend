from ads.models import Banner, Imput


def banner_model(
    text: str = "Gozle Portal",
    description: str = "Market where you can buy computer games and apps",
    link: str = "https://store.gozle.com.tm/",
    min_age: int = 12,
    max_age: int = 18,
    duration: int = 100,
    **kwargs
):
    banner = Banner(
        text=text, description=description, link=link, min_age=min_age, max_age=max_age, duration=duration
    )

    return banner


def create_banner(
    text: str = "Gozle Portal",
    description: str = "Market where you can buy computer games and apps",
    link: str = "https://store.gozle.com.tm/",
    min_age: int = 12,
    duration: int = 100,
    **kwargs
):
    banner = Banner.objects.create(
        text=text, description=description, link=link, min_age=min_age, duration=duration
    )

    return banner


def create_imput(
    link: str = "https://store.gozle.com.tm/",
    duration: int = 100,
    **kwargs
):
    imput = Imput.objects.create(link=link, duration=duration)

    return imput
