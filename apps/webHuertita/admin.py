from django.contrib import admin
from .models import * 

# Register your models here.
admin.site.register(Productos)
admin.site.register(Categorias)
admin.site.register(Usuarios)
admin.site.register(venta)