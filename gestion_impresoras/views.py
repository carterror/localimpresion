from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Local, Impresora, DocumentoSubido
from .forms import LocalForm, ImpresoraForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import smtplib
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.admin.options import get_content_type_for_model
from usuarios.models import Usuario

# create mail object

API_MAILER='mlsn.c802223a14ff82dc5d4ccc46fa579a73118bbe541741af2e6318556974c03327'

# Create your views here.
@login_required
@staff_member_required
def home(request):
    logs = LogEntry.objects.all()
    documentos = DocumentoSubido.objects.count()
    users = Usuario.objects.count()
    locales = Local.objects.count()
    lista = {
    'impresos' : DocumentoSubido.objects.filter(estado='p').count(),
    'pendientes' : DocumentoSubido.objects.filter(estado='i').count()
    }
    return render(request, 'home.html', {'logs': logs, 'documentos': documentos, 'users': users, 'locales': locales, 'lista': lista  })

@login_required
@staff_member_required
def lista_locales(request):
    ruta = 'locaasdl'
    print(ruta.find('local'))
    locales = Local.objects.all()
    return render(request, 'locales/lista_locales.html', {'locales': locales})

@login_required
@staff_member_required
def detalle_local(request, pk):
    local = get_object_or_404(Local, pk=pk)
    return render(request, 'locales/detalle_local.html', {'local': local})

@login_required
@staff_member_required
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

@login_required
@staff_member_required
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

@login_required
@staff_member_required
def eliminar_local(request, pk):
    local = get_object_or_404(Local, pk=pk)

    if request.method == "POST":
        local.delete()
        messages.success(request, 'Local eliminado con éxito.')
        return redirect('lista_locales')
    return render(request, 'locales/eliminar_local.html', {'local': local})

@login_required
@staff_member_required
def lista_impresoras(request):
    impresoras = Impresora.objects.all()
    return render(request, 'impresoras/lista_impresoras.html', {'impresoras': impresoras})

@login_required
@staff_member_required
def detalle_impresora(request, pk):
    impresora = get_object_or_404(Impresora, pk=pk)
    return render(request, 'impresoras/detalle_impresora.html', {'impresora': impresora})

@login_required
@staff_member_required
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

@login_required
@staff_member_required
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

@login_required
@staff_member_required
def eliminar_impresora(request, pk):
    impresora = get_object_or_404(Impresora, pk=pk)

    if request.method == "POST":
        impresora.delete()
        messages.success(request, 'Impresora eliminado con éxito.')
        return redirect('lista_impresoras')
    return render(request, 'impresoras/eliminar_impresora.html', {'impresora': impresora})

@login_required
@staff_member_required
def lista_documentos(request):
    documentos = DocumentoSubido.objects.all()
    return render(request, 'documentos/lista_documento.html', {'documentos': documentos})

@login_required
@staff_member_required
def detalle_documento(request, pk):
    documento = get_object_or_404(documento, pk=pk)
    return render(request, 'documentos/detalle_documento.html', {'documento': documento})

@login_required
@staff_member_required
def editar_documento(request, pk):
    documento = get_object_or_404(DocumentoSubido, pk=pk)
    LogEntry.objects.create(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(documento).pk,
            object_id=str(pk),
            object_repr=str(documento)[:200],
            action_flag=CHANGE,
            change_message='Documento estado Impreso',
        )
    if documento.estado == 'p':
        documento.estado = 'i'
        messages.success(request, 'Documento estado Impreso')

        import mailtrap as mt

        mail = mt.Mail(
            sender=mt.Address(email="mailtrap@demomailtrap.com", name="Servicio de Impresión"),
            to=[mt.Address(email=documento.usuario.email)],
            subject="Confirmación de Impresión de Su Documento",
            text=f"""
Estimado cliente,

Nos complace informarle que su documento ha sido impreso con éxito. A continuación, encontrará los detalles de su impresión:

Nombre del Documento: {documento.titulo}
Fecha y Hora de Impresión: {documento.fecha_subida}
Número de Páginas Impresas: {documento.numero_paginas}
Le recordamos que puede recoger su documento impreso en nuestra sucursal más cercana o, si seleccionó la opción de entrega, estará en camino a la dirección proporcionada durante el proceso de pedido.

Si tiene alguna pregunta o necesita asistencia adicional, no dude en contactarnos a través de nuestro correo electrónico de soporte.

Agradecemos su confianza en nuestro servicio de impresiones automáticas y esperamos seguir siendo su elección preferida para futuras necesidades de impresión.

Atentamente,

            """,
            category="Notification",
        )

        client = mt.MailtrapClient(token="92f94f75a505ab7d038deb2b3551d7e4")
        # client.send(mail)
    else:
        documento.estado = 'p'
        messages.info(request, f'el Documento "{documento.titulo}" se revirtio el estado')
    
    documento.save()
    
    return redirect('lista_documentos')


@login_required
@staff_member_required
def eliminar_documento(request, pk):
    documento = get_object_or_404(DocumentoSubido, pk=pk)

    if request.method == "POST":
        documento.delete()
        LogEntry.objects.create(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(documento).pk,
            object_id=str(pk),
            object_repr=str(documento)[:200],
            action_flag=DELETION,
            change_message='Documento estado Impreso',
        )
        messages.success(request, 'Documento eliminado con éxito.')
        return redirect('lista_documentos')
    return render(request, 'documentos/eliminar_documento.html', {'documento': documento})