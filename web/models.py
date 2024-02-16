from django.db import models
from ckeditor.fields import RichTextField
from usuarios.models import Usuario


class Notice(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    descripcion = RichTextField(null=False)
    user = models.ForeignKey(Usuario, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
