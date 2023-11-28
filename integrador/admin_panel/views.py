from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.contrib import messages

# DECORADORES (averiguar bien luego como implementarlos)
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout

# IMPORTACIONES CBV
from django.views.generic import TemplateView, DeleteView, UpdateView, CreateView

# IMPORTACIONES MODELOS
from . import models, forms


#PANEL DE CONTROL
class ProductsPanelView(TemplateView): 
    template_name = 'admin_panel/products_panel.html'
    
    
    def get(self, request):
        
        products = models.Product.objects.all()
        tags = models.Tag.objects.all() 

        tags_with_products = {}
        for tag in tags:
            products_for_tag = tag.product_list.all()
            tags_with_products[tag] = products_for_tag
            
        ctx = {'products' : products, 'tags': tags, 'tags_with_products': tags_with_products}
        return render(request, self.template_name, ctx)


#PANEL DE CLIENTES
class CustomersPanelView(TemplateView): 
    template_name = 'admin_panel/customers_panel.html'
    
    def get(self, request):  
        customers =  models.Customer.objects.all() 
        ctx = {'customers' : customers}
        return render(request, self.template_name, ctx)




#VISTAS CREATE -> PRODUCTO, TAG, DOMICILIO, CLIENTE 

class ProductCreateView(CreateView):
    model = models.Product
    form_class = forms.ProductForm
    template_name = 'admin_panel/CRUD/product/product_form.html'

    def form_valid(self, form):
        self.object = form.save()
        return redirect('product-panel')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Guardar"
        return context
    

class TagCreateView(CreateView):
    model = models.Tag
    form_class = forms.TagForm
    template_name = 'admin_panel/CRUD/tag/tag_form.html'

    def form_valid(self, form):
        self.object = form.save()
        return redirect('product-panel')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Guardar"
        return context
    
    
class AddressCreateView(CreateView):
    model = models.Address
    form_class = forms.AddressForm
    template_name = 'admin_panel/CRUD/address/address_form.html'

    def form_valid(self, form):
        customer_id = self.kwargs.get('pk') 
        if customer_id:
            customer = get_object_or_404(models.Customer, id=customer_id)
            customer.address = form.save()
            customer.save()
            return redirect('client-panel')
        else:
            self.object = form.save()
            return redirect('client-create', self.object.id)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Guardar"
        return context
      
    
class CustomerCreateView(CreateView):
    model = models.Customer
    form_class = forms.CustomerForm
    template_name = 'admin_panel/CRUD/customer/customer_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.address = models.Address.objects.get(pk=self.kwargs.get('pk'))
        self.object.save()
        return redirect('client-panel')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Guardar"
        return context  
    


#VISTAS UPDATE -> PRODUCTO, TAG, DOMICILIO, CLIENTE

class ProductUpdateView(UpdateView):
    model = models.Product
    form_class = forms.ProductForm
    template_name = 'admin_panel/CRUD/product/product_update.html'

    def form_valid(self, form):
        self.object = form.save()
        return redirect('product-panel')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Actualizar"
        return context
    
    
class TagUpdateView(UpdateView):
    model = models.Tag
    form_class = forms.TagForm
    template_name = 'admin_panel/CRUD/tag/tag_update.html' 
    
    def form_valid(self, form):
        self.object = form.save()
        return redirect('product-panel')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Actualizar"
        return context
    
    
class AddressUpdateView(UpdateView):
    model = models.Address
    form_class = forms.AddressForm
    template_name = 'admin_panel/CRUD/address/address_update.html' 
    
    def form_valid(self, form):
        self.object = form.save()
        return redirect('client-panel')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Actualizar"
        return context
    
class CustomerUpdateView(UpdateView):
    model = models.Customer
    form_class = forms.CustomerForm
    template_name = 'admin_panel/CRUD/customer/customer_update.html' 
    
    def form_valid(self, form):
        self.object = form.save()
        return redirect('client-panel')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Actualizar"
        return context
    
    
    

#VISTAS DELETE -> PRODUCTO, TAG, DOMICILIO, CLIENTE 
    
class ProductDeleteView(DeleteView):
    model = models.Product
    template_name = 'admin_panel/CRUD/product/product_delete.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = self.get_success_url()
        context['message'] = "¿Estás seguro de que deseas eliminar este producto?"
        return context
    
    def get_success_url(self):
        return reverse_lazy('product-panel')


class TagDeleteView(DeleteView):
    model = models.Tag
    template_name = 'admin_panel/CRUD/tag/tag_delete.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = self.get_success_url()
        context['message'] = "¿Estás seguro de que deseas eliminar esta categoría?"
        return context
    
    def get_success_url(self):
        return reverse_lazy('product-panel')
    
    def delete(self, request, *args, **kwargs):
        tag = self.get_object()
        if tag.pk in (1, 2, 3):
            return HttpResponseForbidden("No se puede eliminar esta categoría.")
        return super().delete(request, *args, **kwargs)
    
    
class AddressDeleteView(DeleteView):
    model = models.Address
    template_name = 'admin_panel/CRUD/address/address_delete.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = self.get_success_url()
        context['message'] = "¿Estás seguro de que deseas eliminar este domicilio?"
        return context
    
    def get_success_url(self):
        return reverse_lazy('client-panel')
    
    
class CustomerDeleteView(DeleteView):
    model = models.Customer
    template_name = 'admin_panel/CRUD/customer/customer_delete.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = self.get_success_url()
        context['message'] = "¿Estás seguro de que deseas eliminar al cliente?"
        return context
    
    def get_success_url(self):
        return reverse_lazy('client-panel')
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        address = self.object.address
        if address:
            address.delete()
        return super().delete(request, *args, **kwargs)