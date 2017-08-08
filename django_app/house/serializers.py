from rest_framework import serializers

from house.models import House, Room, PhotoGroup, SearchTag, Category, HousePhoto


class CategorySerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Category
        fields = (
            'id',
            'name'
        )


class SearchTagSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = SearchTag
        fields = (
            'id'
            'name'
        )


class RoomSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Room
        fields = (
            'id',
            'house',
            'name',
            'sex',
            'capacity',
            'area',
            'month_rent',
            'month_manage_fee',
            'pre_util_charge',
            'deposit',
            'moving_month',
            'is_open',
            # 'position',
        )


class HousePhotoSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = HousePhoto
        fields = (
            'id',
            'photo',
        )


class PhotoGroupSerializer(serializers.ModelSerializer):
    """"""
    house_photo = HousePhotoSerializer(many=True, source='housephoto_set')

    class Meta:
        model = PhotoGroup
        fields = (
            'id',
            'house',
            'name',
            'house_photo',
            # 'position',
        )


class HouseDetailSerializer(serializers.ModelSerializer):
    """"""
    rooms = RoomSerializer(many=True, source='room_set')
    province = serializers.SlugRelatedField(slug_field='name', read_only=True)
    city = serializers.SlugRelatedField(slug_field='name', read_only=True)
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    search_tag = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    photo_group = PhotoGroupSerializer(many=True, source='photogroup_set', read_only=True)

    class Meta:
        model = House
        fields = (
            'id',
            'main_title',
            'house_name',
            'capacity_count',
            'main_photo',
            'introduction',
            'opened_date_char',
            'category',
            'province',
            'city',
            'address',
            'position',
            'common_service',
            'private_service',
            'transportation',
            'accessibility',
            'amenity',
            'search_tag',
            'status',
            # 'my_order',
            'rooms',
            'photo_group',
        )


class HouseSerializer(serializers.ModelSerializer):
    """"""
    # rooms = RoomSerializer(many=True, source='room_set')
    province = serializers.SlugRelatedField(slug_field='name', read_only=True)
    city = serializers.SlugRelatedField(slug_field='name', read_only=True)
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    search_tag = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    # photo_group = PhotoGroupSerializer(many=True, source='photogroup_set', read_only=True)

    class Meta:
        model = House
        fields = (
            'id',
            'main_title',
            'house_name',
            'capacity_count',
            'main_photo',
            # 'introduction',
            'opened_date_char',
            'category',
            'province',
            'city',
            'address',
            'position',
            # 'common_service',
            # 'private_service',
            # 'transportation',
            # 'accessibility',
            # 'amenity',
            'search_tag',
            'status',

            # 'my_order',
            # 'rooms',
            # 'photo_group',
        )