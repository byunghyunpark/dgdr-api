from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from main.models import TopBanner, News, TenantFAQ, PartnerFAQ


class TopBannerAdmin(admin.ModelAdmin):
    list_display = (
        "id", "text",
    )


class NewsAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = (
        "id", "title",
    )


class TenantFAQAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = (
        "id", "question",
    )


class PartnerFAQAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = (
        "id", "question",
    )


admin.site.register(TopBanner, TopBannerAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(TenantFAQ, TenantFAQAdmin)
admin.site.register(PartnerFAQ, PartnerFAQAdmin)
