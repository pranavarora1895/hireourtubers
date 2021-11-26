from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html
# Register your models here.

class YoutuberAdmin(admin.ModelAdmin):
    def myphoto(self, object):
           return format_html('<img src="{}" width="40"/>'.format(object.photo.url))

    list_display = ('id','name','price', 'subs_count','is_featured', 'category', 'myphoto',)
    list_display_links = ('name', 'id','category',)
    search_fields = ('name','category','camera_type',)
    list_filter  = ('category', 'is_featured',)
    list_editable = ('is_featured',)



admin.site.register(Youtuber, YoutuberAdmin)