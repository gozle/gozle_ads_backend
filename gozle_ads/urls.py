"""gozle_ads URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django_otp.admin import OTPAdminSite
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from gozle_ads import settings

if settings.DEBUG is False:
    admin.site.__class__ = OTPAdminSite

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('gozle-admin/', admin.site.urls),

    path("api/v1/", include("ads.urls")),
    path("api/v1/", include("authentication.urls")),
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/v1/schema/docs/", SpectacularSwaggerView.as_view(url_name="schema")),

    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [path("__debug__", include("debug_toolbar.urls"))]
