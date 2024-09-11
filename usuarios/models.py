from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

ESTADOS = [
        ('p', 'Pendiente'),
        ('d', 'Denegado'),
        ('a', 'Aceptado'),
    ]

class Usuario(AbstractUser):
    # Aquí puedes añadir campos adicionales si son necesarios
    limites = models.BooleanField(default=True)


class Solicitud(models.Model):
    usuario = models.ForeignKey(Usuario, null=True, on_delete=models.CASCADE)
    estado = models.CharField(default='p', choices=ESTADOS, max_length=2)
    cargo = models.CharField(max_length=100)
    descripcion = models.TextField()
    
    def __str__(self) -> str:
        return f'Solicitud de {self.usuario.username} {self.cargo}'