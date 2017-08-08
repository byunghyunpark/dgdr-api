from django.conf.urls import url

from inquiry.views import TenantInquiryCreateView, PartnerInquiryCreateView

urlpatterns = [
    url(r'^tenant/$', TenantInquiryCreateView.as_view(), name='tenant_create'),
    url(r'^partner/$', PartnerInquiryCreateView.as_view(), name='partner_create'),
]
