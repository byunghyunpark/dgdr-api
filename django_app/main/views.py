from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import TenantFAQ, PartnerFAQ, News, TopBanner
from main.serializers import TenantFAQSerializer, PartnerFAQSerializer, NewsSerializer


class TenantFAQView(ListAPIView):
    """"""
    queryset = TenantFAQ.objects.all()
    serializer_class = TenantFAQSerializer


class PartnerFAQView(ListAPIView):
    """"""
    queryset = PartnerFAQ.objects.all()
    serializer_class = PartnerFAQSerializer


class NewsView(ListAPIView):
    """"""
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class TopBannerView(APIView):
    """"""
    @staticmethod
    def get(request, format=None):
        results = TopBanner.objects.filter(is_active=True)
        if results:
            return Response({"text": results[0].text})
        else:
            return Response({"text": None})
