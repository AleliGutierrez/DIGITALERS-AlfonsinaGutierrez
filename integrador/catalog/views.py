from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib import messages

# IMPORTACIONES CBV
from django.views.generic import TemplateView, ListView,  DetailView

# IMPORTACIONES MODELOS
from admin_panel import models

# IMPORTACIONES FORMULARIOS
from .forms import SearchForm


# HOME / INDEX
class HomeView(TemplateView):
    model = models.Tag
    template_name = "catalog/index.html"
    context_object_name = 'tag'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['acuario'] = models.Tag.objects.get(name='Acuario')
        context['terrario'] = models.Tag.objects.get(name='Terrario')
        context['decoracion'] = models.Tag.objects.get(name='Decoración')
        
        return context

    def get_object(self, queryset=None):
       tag_id = self.kwargs['pk']
       return models.Tag.objects.get(pk=tag_id)
   

#LISTADO DE PRODUCTOS (FILTRADOS POR CATEGORÍA)
class TagProductList(DetailView):
    model = models.Tag
    template_name = 'catalog/category.html'
    context_object_name = 'tag'

    def get_object(self, queryset=None):
       tag_id = self.kwargs['pk']
       return models.Tag.objects.get(pk=tag_id)
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_list'] = self.get_object().product_list.all
        return context 
   
   
#LISTADO DE PRODUCTOS (TODOS)
class ProductList(ListView):
    model = models.Product
    template_name = 'catalog/category.html'
    
    def get_queryset(self):
        search_query = self.kwargs.get('search_query')
        if search_query:
            return search_query
        return models.Product.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.kwargs.get('search_query', None)
        
        if search_query:
            # Si se proporciona search_query, actualiza product_list en consecuencia
            context['product_list'] = models.Product.objects.filter(name__icontains=search_query)
        else:
            # Si no se proporciona search_query, obtén todos los productos
            context['product_list'] = models.Product.objects.all()
        return context  
    
     
#DETALLES PRODUCTO
class ProductDetailView(DetailView):
    model = models.Product
    template_name = 'catalog/product.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
       product_id = self.kwargs['pk']
       return models.Product.objects.get(pk=product_id)


#BÚSQUEDA
def search_view(request):
    """
    Si se ha enviado un formulario, se evalúa que sea válido y se busca productos o tags que contengan 
    el valor enviado, de haber alguna coincidencia se invoca a la vista correspondiente y esta enseña los resultados.
    """
    if request.method == 'POST':
        
        form = SearchForm(request.POST)
    
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
        
            products = models.Product.objects.filter(name__icontains=search_query)
            if products:
                return redirect('product-search', search_query)
        
            tag = models.Tag.objects.filter(name__icontains=search_query).first()
            if tag:
                return redirect('category', tag.id)

            
    return redirect(request.META.get('HTTP_REFERER', 'home'))    
        
    
#ABOUT
class AboutView(TemplateView):
    template_name = "catalog/about.html"
    
    