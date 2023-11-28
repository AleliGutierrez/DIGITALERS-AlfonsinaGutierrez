from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth import login


# IMPORTACIONES CBV
from django.views import View
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, TemplateView, DeleteView, UpdateView


# MODELOS
from . import models
from django.contrib.auth.models import User

# FORMULARIOS
from . import forms
from django.contrib.auth.forms import UserCreationForm

# DECORADORES
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


#PERFIL
@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'user_manager/profile.html'
    
    def get(self, request):  
        user = get_object_or_404(User, username=request.user)
        profile = get_object_or_404(models.Profile, user=user)

        ctx = {
            'profile': profile,
            'username': user.username,
        }

        return render(request, self.template_name, ctx)
    

#USUARIO -> LOGIN / SIGNUP
class MyLoginView(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_invalid(self, form):
        messages.error(self.request, "El usuario o contraseña son inválidos")
        return self.render_to_response(self.get_context_data(form=form))
    
class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        models.Profile.objects.create(user=self.object)
        return response
    
    


# PERFIL -> UPDATE / DELETE
    

class ProfileUpdateView(UpdateView):
    model = models.Profile
    form_class = forms.ProfileForm
    template_name = 'user_manager/CRUD/profile_update.html'
    
    def form_valid(self, form):
        self.object = form.save()
        return redirect('profile')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Actualizar"
        return context  
    
    
class ProfileDeleteView(DeleteView):
    model = models.Profile
    template_name = 'user_manager/CRUD/profile_delete.html'
    
    def delete(self, request, *args, **kwargs):
        profile = self.get_object()
        user = profile.user

       
        if user.username == 'admin':
            return HttpResponseForbidden("Este perfil no puede ser eliminado.")

        response = super().delete(request, *args, **kwargs)
        user.delete()
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = self.get_success_url()
        context['message'] = "¿Estás seguro de que deseas eliminar tu perfil?"
        return context
    
    def get_success_url(self):
        return reverse_lazy('home')
    
    