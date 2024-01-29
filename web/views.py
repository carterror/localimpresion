import PyPDF2
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from gestion_impresoras.models import DocumentoSubido, Local


# Create your views here.
def home(request):
    documentos = DocumentoSubido.objects.all()
    return render(request, 'web/home.html', {'documentos': documentos})


@login_required
def imprimir(request):
    if request.method == 'GET':
        print(Local)
        return render(request, 'web/imprimir.html', {'locales': Local.objects.all()})
    elif request.method == 'POST':
        file = request.FILES['document']
        if file.content_type != 'application/pdf' and not file.name.endswith('.pdf'):
            print('error')
            messages.error(request, 'Por cuestiones de seguridad solo se pueden subir archivos PDF')
            return redirect('/imprimir')

        doscaras = 'doscaras' in request.POST
        color = 'color' in request.POST

        document = DocumentoSubido()
        document.usuario = request.user
        document.titulo = file.name
        document.archivo = file
        document.tipo = file.content_type
        document.color = color
        document.local = Local.objects.get(pk=request.POST['local'])
        document.doscaras = doscaras
        document.numero_copias = request.POST['numero_copias']

        document.save()
        messages.success(request, 'Documento creado con exito')

        return redirect('/')
