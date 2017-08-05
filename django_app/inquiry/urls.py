from django.conf.urls import url

from inquiry.views import TenantInquiryCreateView

urlpatterns = [
    url(r'^tenant/$', TenantInquiryCreateView.as_view(), name='tenant_create'),
]
