from django.contrib import admin
from .models import Car
from django.utils.html import format_html

class CarAdmin(admin.ModelAdmin):
    #affichage photo dans admin
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px" />'.format(object.photo_1.url))
    
    thumbnail.short_description = 'photo_1'
    
    list_display = ('id', 'thumbnail', 'name', 'price', 'is_featured', 'created_date')
    list_display_links = ('id', 'name', 'price')
    search_fields = ('name', 'price', 'is_featured')
    list_filter = ('name', 'is_featured', 'created_date')
    list_editable = ('is_featured',)


admin.site.register(Car, CarAdmin)