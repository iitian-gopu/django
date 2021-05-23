from django.contrib import admin
from testapp.models import filtermodel
# Register your models here.
class FilterModeladmin(admin.ModelAdmin):
    list_display=['name', 'subject', 'dept','date']

admin.site.register(filtermodel,FilterModeladmin)    
