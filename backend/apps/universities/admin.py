
# Register your models here.
from django.contrib import admin
from .models import University, Campus


class CampusInline(admin.TabularInline):
    model = Campus
    extra = 1


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'location_name')
    search_fields = ('name', 'location_name')
    inlines = [CampusInline]


@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ('name', 'university', 'latitude', 'longitude')
    list_filter = ('university',)
    search_fields = ('name', 'university__name')