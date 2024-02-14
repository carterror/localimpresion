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

from django.contrib.auth import views as auth_views
from django.urls import path, include

from apps.reservas.views import (lista_rutas, agregar_ruta, 
                                 editar_ruta, eliminar_ruta,
                                 lista_viajeros, agregar_viajero,
                                 editar_viajero, eliminar_viajero, home)

urlpatterns = [
    path('', home, name='home'),
    
    path('rutas/', lista_rutas, name='lista_rutas'),
    path('rutas/agregar/', agregar_ruta, name='agregar_ruta'),
    path('rutas/<int:pk>/editar/', editar_ruta, name='editar_ruta'),
    path('rutas/<int:pk>/eliminar/', eliminar_ruta, name='eliminar_ruta'),

    path('viajeros/', lista_viajeros, name='lista_viajeros'),
    path('viajeros/agregar/', agregar_viajero, name='agregar_viajero'),
    path('viajeros/<int:pk>/editar/', editar_viajero, name='editar_viajero'),
    path('viajeros/<int:pk>/eliminar/', eliminar_viajero, name='eliminar_viajero'),
]
