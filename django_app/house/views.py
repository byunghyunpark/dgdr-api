from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView

from house.models import House
from house.serializers import HouseSerializer, HouseDetailSerializer


class HouseView(ListAPIView):
    """"""
    serializer_class = HouseSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('is_main', 'is_immediately', 'province', 'city', )

    def get_queryset(self):
        result = House.objects.all().exclude(status="close")
        return result


class HouseDetailView(RetrieveAPIView):
    """"""
    queryset = House.objects.all()
    serializer_class = HouseDetailSerializer
