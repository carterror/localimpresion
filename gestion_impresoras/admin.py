from django.contrib import admin

from gestion_impresoras.models import Impresora, Local, RegistroActividad

# Register your models here.

# Opción 1: Registro Básico
# admin.site.register(Impresora)
# admin.site.register(Local)
# admin.site.register(RegistroActividad)


# Opción 2: Registro Personalizado con Clases
class ImpresoraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'modelo_fabricacion', 'local')
    search_fields = ('nombre', 'marca')
    list_filter = ('marca', 'local')


class LocalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'usuario_encargado')
    search_fields = ('nombre', 'direccion')


class RegistroActividadAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'impresora')
    search_fields = ('fecha', 'descripcion')


admin.site.register(Impresora, ImpresoraAdmin)
admin.site.register(Local, LocalAdmin)
admin.site.register(RegistroActividad, RegistroActividadAdmin)
