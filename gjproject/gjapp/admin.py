from django.contrib import admin
from gjapp.models import blorejobs,kolkatajobs,chennaijobs,punejobs
# Register your models here.
class kolkatajobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','phone'
    ,'email']

class blorejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','phone'
    ,'email']

class punejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','phone'
    ,'email']

class chennaijobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','phone'
    ,'email']

admin.site.register(kolkatajobs,kolkatajobsAdmin)
admin.site.register(blorejobs,blorejobsAdmin)
admin.site.register(chennaijobs,chennaijobsAdmin)
admin.site.register(punejobs,punejobsAdmin)
