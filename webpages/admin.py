from django.contrib import admin
from .models import Slider, Team, About
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin):

    def myphoto(self, object):
       return format_html('<img src="{}" width="40"/>'.format(object.photo.url))


    list_display = ('id','first_name','last_name', 'role','created_date', 'myphoto')
    list_display_links = ('first_name', 'id','myphoto',)
    search_fields = ('first_name','role',)
    list_filter  = ('first_name','role',)



# Register your models here.
admin.site.register(Slider)
admin.site.register(Team, TeamAdmin)
admin.site.register(About)