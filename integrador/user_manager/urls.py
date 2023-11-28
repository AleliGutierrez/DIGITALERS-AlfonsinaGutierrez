#TRATAMIENTO DE LAS URLS
from django.urls import path
from store import settings

#VISTAS
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    # LOG IN
    path('login/', views.MyLoginView.as_view(), name='login'),
    # LOG OUT
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    # SIGN UP 
    path('signup/', views.SignUpView.as_view(), name='signup'),
    
    
    # PERFIL 
    path('profile/', views.ProfileView.as_view(), name='profile'),
    # UPDATE -> PERFIL
    path('profile/modify/<int:pk>/', views.ProfileUpdateView.as_view(), name='profile-update'),
    # DELETE -> PERFIL
    path('profile/delete/<int:pk>/', views.ProfileDeleteView.as_view(), name='profile-delete'),
] 

if settings.DEBUG: 
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)