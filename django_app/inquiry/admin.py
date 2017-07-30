from django.contrib import admin

from inquiry.models import PartnerInquiry, TenantInquiry


class PartnerInquiryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'phone_number', 'email', 'address', 'status', 'inquiry_route', 'created_date'
    )
    list_filter = ("status", )
    search_fields = ("name", )


class TenantInquiryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'house', 'room',
        'moving_date', 'sex', 'name', 'phone_number', 'email', 'is_tenant', 'created_date'
    )
    list_filter = ("house__name", "is_tenant", )
    search_fields = ("name", )


admin.site.register(PartnerInquiry, PartnerInquiryAdmin)
admin.site.register(TenantInquiry, TenantInquiryAdmin)
