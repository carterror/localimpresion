import PyPDF2
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from gestion_impresoras.models import DocumentoSubido, Local, Impresora

from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.admin.options import get_content_type_for_model

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        documentos = DocumentoSubido.objects.filter(usuario=request.user).all()
    else:
        documentos = []
    return render(request, 'web/home.html', {'documentos': documentos})

# Create your views here.
def locales(request):
    locales = Local.objects.all()
    return render(request, 'web/locales.html', {'locales': locales})


@login_required
def imprimir(request, id):
    pendientes = DocumentoSubido.objects.filter(usuario=request.user, estado='p', impresora__local=id).count()
    
    if pendientes >= 3 and request.user.limites:
        messages.error(request, 'Ya usted tiene 3 documentos para imprimir en la cola.')
        return redirect('/')
    
    if request.method == 'GET':
        return render(request, 'web/imprimir.html', {'impresoras': Impresora.objects.filter(local=id).all()})
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
        document.impresora = Impresora.objects.get(pk=request.POST['impresora'])
        document.doscaras = doscaras
        document.numero_copias = request.POST['numero_copias']

    
        document.save()
        LogEntry.objects.create(
                user_id=request.user.pk,
                content_type_id=get_content_type_for_model(document).pk,
                object_id=str(document.pk),
                object_repr=str(document)[:200],
                action_flag=ADDITION,
                change_message='Documento estado Impreso',
            )
        messages.success(request, 'Documento creado con exito')

        return redirect('/')
