from django.conf.urls import url

from house.views import HouseView, HouseDetailView

urlpatterns = [
    url(r'^$', HouseView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', HouseDetailView.as_view(), name='detail')
]
