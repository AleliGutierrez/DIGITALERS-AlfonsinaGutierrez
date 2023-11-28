#TRATAMIENTO DE LAS URLS
from django.urls import path
from store import settings

from . import views

urlpatterns = [
    
    #PANEL DE CLIENTES
    path('client/panel/', views.CustomersPanelView.as_view(), name='client-panel'),
    #PANEL DE PRODUCTOS 
    path('product/panel/', views.ProductsPanelView.as_view(), name='product-panel'),
    
    
    #CREACIÓN DE MODELOS -> CLIENTE(DATOS PERSONALES), DOMICILIO, PRODUCTO, TAG
    path('customer/create/<int:pk>/', views.CustomerCreateView.as_view(), name='client-create'),
    path('address/create/', views.AddressCreateView.as_view(), name='client-address-create'),
    path('address/create/<int:pk>/', views.AddressCreateView.as_view(), name='address-create'),
    path('product/create/', views.ProductCreateView.as_view(), name='product-create'),
    path('tag/create/', views.TagCreateView.as_view(), name='tag-create'),
    
    #ACTUALIZACIÓN DE MODELOS -> DOMICILIO, CLIENTE, PRODUCTO, TAG
    path('address/modify/<int:pk>/', views.AddressUpdateView.as_view(), name='client-address-update'),
    path('customer/modify/<int:pk>/', views.CustomerUpdateView.as_view(), name='client-update'),
    path('product/modify/<int:pk>/', views.ProductUpdateView.as_view(), name='product-update'),
    path('tag/modify/<int:pk>/', views.TagUpdateView.as_view(), name='tag-update'),
    
    #ELIMINACIÓN DE MODELOS -> DOMICILIO, CLIENTE, 
    path('address/delete/<int:pk>/', views.AddressDeleteView.as_view(), name='client-address-delete'),
    path('customer/delete/<int:pk>/', views.CustomerDeleteView.as_view(), name='client-delete'),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product-delete'),
    path('tag/delete/<int:pk>/', views.TagDeleteView.as_view(), name='tag-delete'),
]

if settings.DEBUG: 
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)