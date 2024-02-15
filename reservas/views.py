from django.shortcuts import render, redirect, get_object_or_404
from reservas.models import Ruta
from reservas.forms import RutaForm
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


# Create your views here.
def lista_rutas(request):
    rutas = Ruta.objects.all()
    return render(request, 'ruta/lista_ruta.html', {'rutas': rutas})


def agregar_ruta(request):
    if request.method == "POST":
        form = RutaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ruta creado con éxito.')
            return redirect('lista_rutas')
    else:
        form = RutaForm()
    return render(request, 'ruta/agregar_ruta.html', {'form': form})


def editar_ruta(request, pk):
    ruta = get_object_or_404(Ruta, pk=pk)
    if request.method == "POST":
        form = RutaForm(request.POST,instance=ruta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ruta editado con éxito.')
            return redirect('lista_rutas')
    else:
        form = RutaForm(instance=ruta)
    return render(request, 'ruta/editar_ruta.html', {'form': form, 'ruta': ruta})


def eliminar_ruta(request, pk):
    ruta = get_object_or_404(Ruta, pk=pk)

    if request.method == "POST":
        ruta.delete()
        messages.success(request, 'Ruta eliminada con éxito.')
        return redirect('lista_rutas')

    return render(request, 'ruta/eliminar_ruta.html', {'ruta': ruta})


def lista_viajeros(request):
    pass


def agregar_viajero(request):
    pass


def editar_viajero(request):
    pass


def eliminar_viajero(request):
    pass


def lista_agencias(request):
    pass

def agregar_agencia(request):
    pass

def editar_agencia(request):
    pass

def eliminar_agencia(request):
    pass