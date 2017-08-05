from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView

from house.models import House
from house.serializers import HouseSerializer, HouseDetailSerializer


class HouseView(ListAPIView):
    """"""
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('city', 'is_main', )


class HouseDetailView(RetrieveAPIView):
    """"""
    queryset = House.objects.all()
    serializer_class = HouseDetailSerializer
