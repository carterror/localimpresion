from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import RegistroUsuarioForm
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
import random
import string

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')  # Redirige a la página de inicio después del registro
    else:
        form = RegistroUsuarioForm()
    return render(request, 'auth/register.html', {'form': form})

from django.views.generic import UpdateView
from django.urls import reverse_lazy
from usuarios.models import Usuario, Solicitud
from usuarios.forms import PerfilForm

class PerfilUpdateView(UpdateView):
    model = Usuario
    form_class = PerfilForm
    template_name = 'web/perfil.html'
    success_url = reverse_lazy('perfil')
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["form2"] = PasswordChangeForm(self.request.user)
        return context

@login_required
@staff_member_required
def lista_limites(request):
    limites = Solicitud.objects.all()
    return render(request, 'limites/lista_limites.html', {'limites': limites})

@login_required
@staff_member_required
def aceptar_limite(request, pk):
    solicitud = Solicitud.objects.get(pk=pk)
    solicitud.estado = 'a'
    solicitud.save()
    user = Usuario.objects.get(pk=solicitud.usuario.pk)
    user.limites = False
    user.save()
    messages.success(request, 'Solicitud Aceptada con éxito')
    return redirect('lista_limites')
    
@login_required
@staff_member_required
def denegar_limite(request, pk):
    solicitud = Solicitud.objects.get(pk=pk)
    solicitud.estado = 'd'
    solicitud.save()
    user = Usuario.objects.get(pk=solicitud.usuario.pk)
    user.limites = True
    user.save()
    messages.success(request, 'Solicitud Denegada con éxito')
    return redirect('lista_limites')

@login_required
def solicitud_limite(request):
    solicitud = Solicitud.objects.create(
        usuario=request.user,
        cargo= request.POST['cargo'],
        descripcion = request.POST['mensaje'],
    )
    messages.success(request, 'Solicitud Enviada con éxito')
    return redirect('perfil')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # To keep the user logged in
            messages.success(request, 'Contraseña actualizada')
            return redirect('perfil')
        else:
            return render(request, 'web/perfil.html', {'form': PerfilForm(), 'form2': form})
        
@login_required
@staff_member_required
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

@login_required
@staff_member_required
def change_pass(request, pk):
    usuario = Usuario.objects.get(pk = pk)
    contra = f'{usuario.username}-{"".join(random.choice(string.ascii_letters) for _ in range(5))}'
    usuario.set_password(contra)
    usuario.save()
    messages.info(request, f'Contraseña restablecida con éxito, nueva contraseña: {contra}')
    return redirect('lista_usuarios')

@login_required
@staff_member_required
def eliminar_user(request, pk):
    usuarios = get_object_or_404(Usuario, pk=pk)

    if request.method == "POST":
        usuarios.delete()
        messages.success(request, 'Usuario eliminado con éxito.')
        return redirect('lista_usuarios')
    return render(request, 'usuarios/eliminar_usuario.html', {'usuarios': usuarios})