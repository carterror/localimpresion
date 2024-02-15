from django.contrib import messages
from django.http import HttpResponse

from django.shortcuts import render, redirect, get_object_or_404
from gestion_impresoras.models import Local, Impresora
from gestion_impresoras.forms import LocalForm, ImpresoraForm


# Create your views here.
def home(request):
    return render(request, 'home.html')


def lista_locales(request):
    ruta = 'locaasdl'
    print(ruta.find('local'))
    locales = Local.objects.all()
    return render(request, 'locales/lista_locales.html', {'locales': locales})


def detalle_local(request, pk):
    local = get_object_or_404(Local, pk=pk)
    return render(request, 'locales/detalle_local.html', {'local': local})


def agregar_local(request):
    if request.method == "POST":
        form = LocalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Local creado con éxito.')
            return redirect('lista_locales')
    else:
        form = LocalForm()
    return render(request, 'locales/agregar_local.html', {'form': form})


def editar_local(request, pk):
    local = get_object_or_404(Local, pk=pk)
    if request.method == "POST":
        form = LocalForm(request.POST, instance=local, local_id=local.id)
        if form.is_valid():
            form.save()
            messages.success(request, 'Local editado con éxito.')
            return redirect('lista_locales')
    else:
        form = LocalForm(instance=local, local_id=local.id)
    return render(request, 'locales/editar_local.html', {'form': form})


def eliminar_local(request, pk):
    local = get_object_or_404(Local, pk=pk)

    if request.method == "POST":
        local.delete()
        messages.success(request, 'Local eliminado con éxito.')
        return redirect('lista_locales')
    return render(request, 'locales/eliminar_local.html', {'local': local})


def lista_impresoras(request):
    impresoras = Impresora.objects.all()
    return render(request, 'impresoras/lista_impresoras.html', {'impresoras': impresoras})


def detalle_impresora(request, pk):
    impresora = get_object_or_404(Impresora, pk=pk)
    return render(request, 'impresoras/detalle_impresora.html', {'impresora': impresora})


def agregar_impresora(request):
    if request.method == "POST":
        form = ImpresoraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Impresora creado con éxito.')
            return redirect('lista_impresoras')
    else:
        form = ImpresoraForm()
    return render(request, 'impresoras/agregar_impresora.html', {'form': form})


def editar_impresora(request, pk):
    impresora = get_object_or_404(Impresora, pk=pk)
    if request.method == "POST":
        form = ImpresoraForm(request.POST, instance=impresora, impresora_id=impresora.id)
        if form.is_valid():
            form.save()
            messages.success(request, 'Impresora editado con éxito.')
            return redirect('lista_impresoras')
    else:
        form = ImpresoraForm(instance=impresora, impresora_id=impresora.id)
    return render(request, 'impresoras/editar_impresora.html', {'form': form})


def eliminar_impresora(request, pk):
    impresora = get_object_or_404(Local, pk=pk)

    if request.method == "POST":
        impresora.delete()
        messages.success(request, 'Local eliminado con éxito.')
        return redirect('lista_impresoras')
    return render(request, 'impresoras/eliminar_impresora.html', {'impresora': impresora})
