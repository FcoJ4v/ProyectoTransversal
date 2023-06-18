from django.shortcuts import render
from .models import *

# Create your views here.

def cargarIndex(request):
    return render(request,"index.html")

def cargarRegistro(request):
    return render(request,"registro.html")


def cargarDatoUsuario(request):
    usuario = Usuarios.objects.all()
    return render(request, "mi_cuenta.html", {"usu":usuario})

def agregarUsuario(request):
    print(request.POST)
    v_rut = request.POST['txtSku']
    v_nombre = request.POST['txtNombre']
    v_appaterno = request.POST['txtPrecio']
    v_apmaterno = request.POST['txtStock']
    v_genero = request.POST['txtDescripcion']
    v_correo = request.POST['txtDescripcion']
    v_celular = request.POST['txtDescripcion']
    v_telefono = request.POST['txtDescripcion']
    v_contraseña = request.POST['txtDescripcion']
    v_direccion = request.POST['txtDescripcion']
    v_numero = request.POST['txtDescripcion']
    v_depto = request.POST['txtDescripcion']
    v_region = request.POST['txtDescripcion']
    v_ciudad = request.POST['txtDescripcion']
    v_comuna = request.POST['txtDescripcion']
 