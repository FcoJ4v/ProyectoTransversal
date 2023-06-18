from django.urls import path
from . import views

urlpatterns =[
    path('index/',views.cargarIndex),
    path('registro',views.cargarRegistro),
    path('mi_cuenta',views.cargarDatoUsuario)
]