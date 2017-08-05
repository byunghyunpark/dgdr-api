from rest_framework import serializers

from inquiry.models import TenantInquiry, PartnerInquiry


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


class PartnerInquirySerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)

    class Meta:
        model = PartnerInquiry
        fields = (
            'id',
            'name',
            'phone_number',
            'email',
            'address',
            'memo',
            'status',
            'inquiry_route',
        )

    def create(self, validated_data):
        instance = self.Meta.model.objects.create(
            inquiry_route="Home page",
            status="waiting",
            **validated_data
        )

        return instance
