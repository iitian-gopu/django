from django.contrib import admin
from testapp.models import movie
# Register your models here.
class movieAdmin(admin.ModelAdmin):
    list_display=['rdate','moviename','hero','heroine','rating']

admin.site.register(movie,movieAdmin)    
