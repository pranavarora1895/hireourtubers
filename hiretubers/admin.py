from django.contrib import admin
from .models import Hiretuber
# Register your models here.

class HiretuberAdmin(admin.ModelAdmin):

    list_display = ('id','first_name','last_name', 'email', 'created_date')
    list_display_links = ('first_name', 'id','email',)
    search_fields = ('email','first_name','phone')
    list_filter  = ('city','state','tuber_name')


admin.site.register(Hiretuber, HiretuberAdmin)
