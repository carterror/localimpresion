from django.contrib import admin
from apps.reservas.models import Ruta, Viajero, Pasaje, Viaje
# Register your models here.
admin.site.register(Ruta)
admin.site.register(Viajero)
admin.site.register(Pasaje)
admin.site.register(Viaje)
