from django.contrib import admin

from region.models import City, Province


class CityInline(admin.StackedInline):
    model = City
    extra = 2


class ProvinceAdmin(admin.ModelAdmin):
    model = Province
    list_display = ('name', 'latitude', 'longitude', 'id', )
    inlines = (CityInline, )


admin.site.register(Province, ProvinceAdmin, )
