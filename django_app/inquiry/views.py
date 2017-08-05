from rest_framework.generics import CreateAPIView

from inquiry.models import TenantInquiry, PartnerInquiry
from inquiry.serializers import TenantInquirySerializer, PartnerInquirySerializer


class TenantInquiryCreateView(CreateAPIView):
    queryset = TenantInquiry
    serializer_class = TenantInquirySerializer


class PartnerInquiryCreateView(CreateAPIView):
    queryset = PartnerInquiry
    serializer_class = PartnerInquirySerializer
