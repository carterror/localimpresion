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
from django.urls import path, include

from gestion_impresoras.views import home, lista_locales, agregar_local, editar_local, eliminar_local, lista_impresoras, \
    agregar_impresora, eliminar_impresora, editar_impresora, lista_documentos, editar_documento, detalle_documento, eliminar_documento

urlpatterns = [
    path('', home, name='dashboard'),

    # path('locales/<int:pk>/', detalle_local, name='detalle_local'),
    path('locales/', lista_locales, name='lista_locales'),
    path('locales/agregar/', agregar_local, name='agregar_local'),
    path('locales/<int:pk>/editar/', editar_local, name='editar_local'),
    path('locales/<int:pk>/eliminar/', eliminar_local, name='eliminar_local'),

    path('impresoras/', lista_impresoras, name='lista_impresoras'),
    path('impresoras/agregar/', agregar_impresora, name='agregar_impresora'),
    path('impresoras/<int:pk>/editar/', editar_impresora, name='editar_impresora'),
    path('impresoras/<int:pk>/eliminar/', eliminar_impresora, name='eliminar_impresora'),

    path('documentos/', lista_documentos, name='lista_documentos'),
    path('documentos/<int:pk>/editar/', editar_documento, name='editar_documento'),
    path('documentos/<int:pk>/', detalle_documento, name='detalle_documento'),
    path('documentos/<int:pk>/eliminar/', eliminar_documento, name='eliminar_documento'),

]
