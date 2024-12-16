from django.contrib import admin
from .models import Turlar, Gullar
from django.utils.safestring import mark_safe

# Register your models here.
admin.site.register(Turlar)

class GulAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'tur', 'color', 'get_images')
    list_display_links = ('name', 'pk')
    list_editable = ('tur',)
    list_filter = ('tur',)
    search_fields = ('pk', 'name', 'about')
    list_per_page = 10

    def get_images(self, gul):
        if gul.photo:
            return mark_safe(f'<img src="{gul.photo.url}" width="150px" />')
        else:
            return '-'
    get_images.short_description = 'Rasmi'

admin.site.register(Gullar, GulAdmin)
