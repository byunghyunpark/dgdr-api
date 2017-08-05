from rest_framework.generics import CreateAPIView

from inquiry.models import TenantInquiry
from inquiry.serializers import TenantInquirySerializer


class TenantInquiryCreateView(CreateAPIView):
    queryset = TenantInquiry
    serializer_class = TenantInquirySerializer
