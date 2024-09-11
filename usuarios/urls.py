"""
URL configuration for localimpresion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.urls import path, include

from usuarios.views import registro, PerfilUpdateView, lista_limites, aceptar_limite, denegar_limite, solicitud_limite, change_password, lista_usuarios, change_pass, eliminar_user

urlpatterns = [
    path('login/', LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('registro/', registro, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('perfil/', PerfilUpdateView.as_view(), name='perfil'),
    path('perfil/change_password', change_password, name='change_password'),
    
    path('limites/', lista_limites, name='lista_limites'),
    path('limites/<int:pk>/aceptar', aceptar_limite, name='aceptar_limite'),
    path('limites/<int:pk>/denegar', denegar_limite, name='denegar_limite'),
    path('limites/solicitud', solicitud_limite, name='solicitud_limite'),
    
    path('usuarios/', lista_usuarios, name='lista_usuarios'),
    path('usuarios/<int:pk>/change_pass', change_pass, name='change_pass'),
    path('usuarios/<int:pk>/eliminar', eliminar_user, name='eliminar_user'),
    
]
