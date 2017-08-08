from django.conf.urls import url

from region.views import RegionView

urlpatterns = [
    url(r'^$', RegionView.as_view(), name='list'),
]
