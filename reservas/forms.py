# gestion_impresoras/forms.py

from django import forms
from django.core.exceptions import ValidationError

from reservas.models import Ruta


class RutaForm(forms.ModelForm):
    lugar = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control my-2'}))
    
    class Meta:
        model = Ruta
        fields = ['lugar']



# class ImpresoraForm(forms.ModelForm):
#     nombre = forms.CharField(required=True,
#                              widget=forms.TextInput(attrs={'class': 'form-control my-2 col-md-6'}))
#     tipo_conexion = forms.ChoiceField(required=True, choices=(
#         ('USB', 'USB'),
#         ('SERIAL', 'SERIAL'),
#         ('WIFI', 'WIFI'),
#     ),
#                                       widget=forms.Select(attrs={'class': 'form-select my-2'})
#                                       )
#     descripcion = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control my-2'}))
#     localizacion = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control my-2'}))
#     marca = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control my-2'}))
#     modelo_fabricacion = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control my-2'}))
#     local = forms.ModelChoiceField(required=True,
#                                    widget=forms.Select(attrs={'class': 'form-select my-2'}),
#                                    queryset=Local.objects.all(),
#                                    empty_label="Selecciona un Impresora")

#     class Meta:
#         model = Impresora
#         fields = [
#             'nombre',
#             'tipo_conexion',
#             'descripcion',
#             'localizacion',
#             'marca',
#             'modelo_fabricacion',
#             'local']

#     def __init__(self, *args, **kwargs):
#         self.impresora_id = kwargs.pop('impresora_id', None)
#         super(ImpresoraForm, self).__init__(*args, **kwargs)
