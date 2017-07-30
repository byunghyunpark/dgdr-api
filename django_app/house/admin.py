from django.contrib import admin
import nested_admin

from house.models import House, SearchTag, PhotoGroup, HousePhoto, Category, Room


class SearchTagAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name"
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name"
    )


class RoomInline(nested_admin.NestedTabularInline):
    model = Room
    sortable_field_name = "position"
    extra = 0


class HousePhotoInline(nested_admin.NestedTabularInline):
    model = HousePhoto
    sortable_field_name = "position"
    extra = 0


class PhotoGroupInline(nested_admin.NestedTabularInline):
    model = PhotoGroup
    sortable_field_name = "position"
    inlines = [HousePhotoInline, ]
    extra = 0


class HouseAdmin(nested_admin.NestedModelAdmin):
    inlines = [RoomInline, PhotoGroupInline, ]
    list_display = (
        "id", "name", "opened_date", "capacity_count", "status"
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(House, HouseAdmin)
admin.site.register(SearchTag, SearchTagAdmin)
