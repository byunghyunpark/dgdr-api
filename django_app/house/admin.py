from django.contrib import admin

from house.models import House, SearchTag


class SearchTagAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name"
    )


class HouseAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "opened_date", "capacity", "category", "status"
    )


admin.site.register(House, HouseAdmin)
admin.site.register(SearchTag, SearchTagAdmin)
