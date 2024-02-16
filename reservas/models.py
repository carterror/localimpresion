from django.db import models


# Create your models here.
class Ruta(models.Model):
    lugar = models.CharField(null=False, max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)


class Viajero(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    ci = models.CharField(max_length=11, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Agencia(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    provincia = models.CharField(max_length=50, null=False)
    telefono = models.CharField(max_length=12, null=False)
    direccion = models.CharField(max_length=250, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Pasaje(models.Model):
    origen = models.ForeignKey(Ruta, null=False, on_delete=models.CASCADE, related_name='origenes')
    destino = models.ForeignKey(Ruta, null=False, on_delete=models.CASCADE, related_name='destinos')
    precio = models.DecimalField(null=False, decimal_places=2, max_digits=10)
    capacidad = models.IntegerField(null=False)
    fecha = models.DateTimeField(null=True)
    transporte = models.CharField(null=False, max_length=20, choices={
        "AV": "Avión",
        "TR": "Tren",
        "BU": "Omnibús",
    })

    def asientos(self):
        ocupados = Viaje.objects.filter(pasaje=self).count()
        return self.capacidad - ocupados

    def tipo(self):
        tipos = {
            "AV": "Avión",
            "TR": "Tren",
            "BU": "Omnibús",
        }
        return tipos[self.transporte]


class Viaje(models.Model):
    pasaje = models.ForeignKey(Pasaje, null=False, on_delete=models.CASCADE)
    viajero = models.ForeignKey(Viajero, null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
