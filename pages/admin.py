from django.contrib import admin
from .models import Team
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin):
    #affichage photo dans admin
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px" />'.format(object.photo.url))
    
    thumbnail.short_description = 'photo'
    
    list_display = ('id', 'thumbnail', 'last_name', 'first_name', 'designation', 'created_date')
    list_display_links = ('id', 'first_name', 'last_name', 'thumbnail')
    search_fields = ('last_name', 'first_name', 'designation')
    list_filter = ('designation',)
    
admin.site.register(Team, TeamAdmin)