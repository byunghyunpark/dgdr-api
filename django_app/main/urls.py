from django.conf.urls import url

from main.views import TenantFAQView, PartnerFAQView, NewsView, TopBannerView

urlpatterns = [
    url(r'^faq/tenant/$', TenantFAQView.as_view(), name='tenant_faq'),
    url(r'^faq/partner/$', PartnerFAQView.as_view(), name='partner_faq'),
    url(r'^news/$', NewsView.as_view(), name='news'),
    url(r'^top-banner/$', TopBannerView.as_view(), name='top_banner'),
]

