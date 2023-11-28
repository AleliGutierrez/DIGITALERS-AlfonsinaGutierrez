from django.db import models
from django.contrib.auth.models import User


# PERFIL
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar =  models.ImageField(upload_to= 'profile_pictures', default='profile_pictures/default_profile.jpeg', verbose_name='Imagen de perfil')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name='Perfil'
        verbose_name_plural='Perfiles'
        
