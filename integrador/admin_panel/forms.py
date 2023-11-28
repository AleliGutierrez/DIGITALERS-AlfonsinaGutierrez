#IMPORTACIONES
from django import forms
from django.template import Template
from django.utils.safestring import mark_safe
from django.forms import ImageField

#MODELOS
from . import models


# PRODUCTO
class ProductForm(forms.ModelForm):
    
    class Meta:
        model = models.Product
        fields = '__all__'
        
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese el nombre del producto:'}),
        'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Ingrese el precio:'}),
        'inventory': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Ingrese el inventario disponible:'}),
        'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Ingrese la descripción:'}),
    }
        
        labels ={
           'name':'', 
           'price':'', 
           'inventory':'', 
           'description':'',
       }
        

        
# TAG
class TagForm(forms.ModelForm):
    class Meta:
        model = models.Tag
        fields = '__all__'
        
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese el nombre de la categoría:'}),
        'product_list': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
        
        labels ={
           'name':'', 
           'product_list':'',
       }
        
        

# CLIENTE
class CustomerForm(forms.ModelForm):
    
    class Meta:
       model = models.Customer
       fields = ['first_name', 'last_name', 'id_number', 'phone']
       
       widgets = {
           'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su nombre:'}), 
           'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su apellido:'}), 
           'id_number': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Ingrese su DNI:'}), 
           'phone': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Ingrese un número de teléfono:'}),
       }
       labels ={
           'first_name':'', 
           'last_name':'', 
           'id_number':'', 
           'phone':'',
       }
       
       def __init__(self, *args, **kwargs):
        address = kwargs.pop('address', None)
        super(CustomerForm, self).__init__(*args, **kwargs)
        if address:
            self.fields['address'].initial = address
       
       
       
# DOMICILIO
class AddressForm(forms.ModelForm):
    class Meta:
        model = models.Address
        fields = '__all__'
        
        widgets = {
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese el país:'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese la provincia:'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese la ciudad:'}),
            'neighborhood': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese el barrio:'}),
            'street': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese la calle:'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese el código postal:'}),
        }
        
        labels ={
           'country':'', 
           'state':'', 
           'city':'', 
           'neighborhood':'',
           'street':'',
           'postal_code':'',
       }