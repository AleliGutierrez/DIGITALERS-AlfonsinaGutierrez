from django.urls import path
from store import settings

#VISTAS
from . import views

urlpatterns = [
    #HOME
    path('', views.HomeView.as_view(), name='home'),

    #VISTAS RELACIONAS A -> PRODUCTOS / PRODUCTOS POR CATEGORÍA / VISTA DETALLADA DEL PRODUCTO
    path('products/', views.ProductList.as_view(), name='products'),
    path('category/<int:pk>/', views.TagProductList.as_view(), name='category'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product'),
    
    #BÚSQUEDAS
    path('search/', views.search_view, name='search'),
    path('products/<str:search_query>/', views.ProductList.as_view(), name='product-search'),
] 

if settings.DEBUG: 
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)