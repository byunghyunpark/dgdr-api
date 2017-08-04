from rest_framework.generics import ListAPIView, RetrieveAPIView

from house.models import House
from house.serializers import HouseSerializer, HouseDetailSerializer


class HouseView(ListAPIView):
    """"""
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class HouseDetailView(RetrieveAPIView):
    """"""
    queryset = House.objects.all()
    serializer_class = HouseDetailSerializer
