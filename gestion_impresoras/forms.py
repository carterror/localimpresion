# gestion_impresoras/forms.py

from django import forms
from django.core.exceptions import ValidationError

from usuarios.models import Usuario
from .models import Local, Impresora, DocumentoSubido


class LocalForm(forms.ModelForm):
    nombre = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control my-2'}))
    direccion = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control my-2'}))
    usuario_encargado = forms.ModelChoiceField(required=True,
                                               widget=forms.Select(attrs={'class': 'form-select my-2'}),
                                               queryset=Usuario.objects.all(),
                                               empty_label="Selecciona un Usuario")

    class Meta:
        model = Local
        fields = ['nombre', 'direccion', 'usuario_encargado']

    def __init__(self, *args, **kwargs):
        self.local_id = kwargs.pop('local_id', None)
        super(LocalForm, self).__init__(*args, **kwargs)

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        queryset = Local.objects.filter(nombre=nombre)

        # Si estamos editando un local (local_id no es None), excluirlo de la verificación
        if self.local_id:
            queryset = queryset.exclude(id=self.local_id)

        if queryset.exists():
            raise ValidationError("Este local ya está en uso.")
        return nombre


class ImpresoraForm(forms.ModelForm):
    nombre = forms.CharField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control my-2 col-md-6'}))
    tipo_conexion = forms.ChoiceField(required=True, choices=(
        ('USB', 'USB'),
        ('SERIAL', 'SERIAL'),
        ('WIFI', 'WIFI'),
    ),
                                      widget=forms.Select(attrs={'class': 'form-select my-2'})
                                      )
    descripcion = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control my-2', 'pattern': "^[^\d].*"}))
    localizacion = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control my-2'}))
    marca = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control my-2'}))
    modelo_fabricacion = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control my-2'}))
    local = forms.ModelChoiceField(required=True,
                                   widget=forms.Select(attrs={'class': 'form-select my-2'}),
                                   queryset=Local.objects.all(),
                                   empty_label="Selecciona un Impresora")

    class Meta:
        model = Impresora
        fields = [
            'nombre',
            'tipo_conexion',
            'descripcion',
            'localizacion',
            'marca',
            'modelo_fabricacion',
            'local']

    def __init__(self, *args, **kwargs):
        self.impresora_id = kwargs.pop('impresora_id', None)
        super(ImpresoraForm, self).__init__(*args, **kwargs)