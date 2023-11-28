from django.contrib import admin
from . import models 


# TAG
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    
admin.site.register(models.Tag, TagAdmin)


# PRODUCTO
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('price', 'name', 'inventory')
    
admin.site.register(models.Product, ProductAdmin)


# CLIENTE
class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('first_name', 'last_name')
    
admin.site.register(models.Customer, CustomerAdmin)


# DOMICILIO-CLIENTE
class AddressAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('country', 'state', 'city')
    
admin.site.register(models.Address, AddressAdmin)