from django.shortcuts import render, redirect

# Create your views here.
# usuarios/views.py

from django.contrib.auth import login, authenticate
from apps.usuarios.forms import RegistroUsuarioForm


def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')  # Redirige a la página de inicio después del registro
    else:
        form = RegistroUsuarioForm()
    return render(request, 'auth/register.html', {'form': form})
