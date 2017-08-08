from rest_framework import serializers

from main.models import TenantFAQ, PartnerFAQ, News, TopBanner


class TenantFAQSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = TenantFAQ
        fields = (
            'id',
            'question',
            'answer',
        )


class PartnerFAQSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = PartnerFAQ
        fields = (
            'id',
            'question',
            'answer',
        )


class NewsSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = News
        fields = (
            'id',
            'title',
            'context',
            'photo',
            'link_url',
        )
