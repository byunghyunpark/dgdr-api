from rest_framework import serializers

from region.models import Province, City


class CitySerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = City
        fields = (
            'id',
            'name',
        )


class ProvinceSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Province
        fields = (
            'id',
            'name',
        )


class RegionSerializer(serializers.ModelSerializer):
    """"""
    cities = CitySerializer(many=True, source='city_set')

    class Meta:
        model = Province
        fields = (
            'id',
            'name',
            'cities',
        )
