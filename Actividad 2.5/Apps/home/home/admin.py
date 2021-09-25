from django.contrib import admin
from .models import Cliente, Estudiante, TipoCliente, Venta

# Register your models here.
admin.site.register(Cliente)
admin.site.register(TipoCliente)
admin.site.register(Venta)
admin.site.register(Estudiante)


