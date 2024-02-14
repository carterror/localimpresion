from django.shortcuts import render
from apps.reservas.models import Ruta

def home(request):
    return render(request, 'home.html')


# Create your views here.
def lista_rutas(request):
    rutas = Ruta.objects.all()
    return render(request, 'ruta/lista_ruta.html', {'rutas': rutas})


def agregar_ruta(request):
    pass

def editar_ruta(request):
    pass

def eliminar_ruta(request):
    pass

def lista_viajeros(request):
    pass

def agregar_viajero(request):
    pass

def editar_viajero(request):
    pass

def eliminar_viajero(request):
    pass
