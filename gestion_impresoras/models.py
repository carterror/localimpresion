from django.db import models

from usuarios.models import Usuario


# Create your models here.
class Local(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    usuario_encargado = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)

    # Aquí puedes añadir otros campos que consideres relevantes

    def __str__(self):
        return self.nombre


class Impresora(models.Model):
    tipo_conexion = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    localizacion = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    modelo_fabricacion = models.CharField(max_length=50)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.marca} {self.modelo_fabricacion}"


class DocumentoSubido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="documentos_subidos")
    titulo = models.CharField(max_length=255)
    archivo = models.FileField(upload_to='uploads/documentos/')
    tipo = models.CharField(max_length=100)
    local = models.ForeignKey(Local, on_delete=models.SET_NULL, null=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)
    color = models.BooleanField(default=False)
    impresora = models.ForeignKey(Impresora, on_delete=models.SET_NULL, null=True)
    doscaras = models.BooleanField(default=False)
    numero_copias = models.IntegerField(default=1)
    numero_paginas = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.titulo} subido por {self.usuario.username}"


class RegistroActividad(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    impresora = models.ForeignKey(Impresora, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fecha} - {self.impresora.nombre} - Actividad"
