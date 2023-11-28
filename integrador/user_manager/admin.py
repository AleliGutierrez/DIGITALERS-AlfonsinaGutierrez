from django.contrib import admin
from . import models

# PERFIL
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated', 'id')
    list_display = ('avatar', 'user')
     
admin.site.register(models.Profile, ProfileAdmin)


    
