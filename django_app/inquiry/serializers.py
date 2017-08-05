from rest_framework import serializers

from inquiry.models import TenantInquiry


class TenantInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantInquiry
        fields = (
            'id',
            'name',
            'sex',
            'phone_number',
            'email',
            'house',
            'room',
            'moving_date',
            'memo',
            # 'is_tenant',
            # 'is_waiting',
        )

    def create(self, validated_data):
        room_obj = validated_data.get('room', None)

        if room_obj.is_open:
            is_waiting = False
        else:
            is_waiting = True

        house_obj = room_obj.house

        instance = self.Meta.model.objects.create(
            house=house_obj,
            is_waiting=is_waiting,
            **validated_data
        )

        return instance
