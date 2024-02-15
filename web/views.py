from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from reservas.models import Ruta, Viaje, Pasaje
from django.db.models.functions import TruncDate

# Create your views here.
def home(request):
    rutas = Ruta.objects.all()
    return render(request, 'web/home.html', {'rutas': rutas})

def buscar(request):
    if request.method == 'POST':
        pasajes = Pasaje.objects.filter(origen=request.POST['origen'], destino=request.POST['destino'])
        if request.POST['fecha']:
            pasajes.annotate(fecha_truncada=TruncDate('fecha')).filter(fecha_truncada=request.POST['fecha'])
        return render(request, 'web/pasaje.html', {'pasajes': pasajes})
    else:
        rutas = Ruta.objects.all()
        return render(request, 'web/buscar.html', {'rutas': rutas})
    