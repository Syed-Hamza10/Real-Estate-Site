from django.contrib import admin
from .models import *
# Register your models here.


class PropertyAdmin(admin.ModelAdmin):
    list_display = ['id','title','area','price']
    list_display_links = ['id','title','area']
    list_filter = ['is_negotiable']

admin.site.register(Property,PropertyAdmin)
admin.site.register(PropertyCategory)
admin.site.register(PropertyFeature)