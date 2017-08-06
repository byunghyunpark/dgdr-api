"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from mysite import settings

urlpatterns = [
    url(r'^dgdr-admin/', admin.site.urls),
    url(r'^nested_admin/', include('nested_admin.urls')),
    url(r'^chaining/', include('smart_selects.urls')),  # django-smart-selects,
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^house/', include('house.urls', namespace='house')),
    url(r'^region/', include('region.urls', namespace='region')),
    url(r'^inquiry/', include('inquiry.urls', namespace='inquiry')),
    url(r'^main/', include('main.urls', namespace='main')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
