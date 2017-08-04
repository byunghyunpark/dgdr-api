from rest_framework.generics import ListAPIView

from region.models import City, Province
from region.serializers import CitySerializer, RegionSerializer
from region.serializers import ProvinceSerializer


class ProvinceView(ListAPIView):
    """"""
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer


class CityView(ListAPIView):
    """"""
    queryset = City.objects.all()
    serializer_class = CitySerializer


class RegionView(ListAPIView):
    """"""
    queryset = Province.objects.all
    serializer_class = RegionSerializer
