import nested_admin
from django import forms
from django.contrib import admin

from common.constants import UPLOAD_PHOTO_MAX_SIZE
from house.models import House, SearchTag, PhotoGroup, HousePhoto, Category, Room


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = "__all__"

    def clean_main_photo(self):
        main_photo = self.cleaned_data.get("main_photo")

        if not main_photo:
            raise forms.ValidationError("No photo!")
        elif main_photo.size > UPLOAD_PHOTO_MAX_SIZE:
            raise forms.ValidationError("Photo size should be less than {SIZE}byte".format(SIZE=UPLOAD_PHOTO_MAX_SIZE))
        else:
            return main_photo


class HousePhotoForm(forms.ModelForm):
    class Meta:
        model = HousePhoto
        fields = "__all__"

    def clean_photo(self):
        photo = self.cleaned_data.get("photo")
        if not photo:
            raise forms.ValidationError("No photo!")
        elif photo.size > UPLOAD_PHOTO_MAX_SIZE:
            raise forms.ValidationError("Photo size should be less than {SIZE}byte".format(SIZE=UPLOAD_PHOTO_MAX_SIZE))
        else:
            return photo


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
    form = HousePhotoForm
    model = HousePhoto
    sortable_field_name = "position"
    extra = 0


class PhotoGroupInline(nested_admin.NestedTabularInline):
    model = PhotoGroup
    sortable_field_name = "position"
    inlines = [HousePhotoInline, ]
    extra = 0


class HouseAdmin(nested_admin.NestedModelAdmin):
    form = HouseForm
    inlines = [RoomInline, PhotoGroupInline, ]
    list_display = (
        "id", "name", "opened_date", "capacity_count", "status"
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(House, HouseAdmin)
admin.site.register(SearchTag, SearchTagAdmin)
