from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
import os
from django.http import HttpResponse
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from apps.webHuertita.Carrito import Carrito

from django.shortcuts import get_object_or_404


# Create your views here.

def cargarIndex(request):
   productos = Producto.objects.all()
   cate_planta = Producto.objects.filter(categoria_id = 1)
   cate_herramienta = Producto.objects.filter(categoria_id = 20)
   return render(request, "index.html", {"prod":productos, "categoria_pla": cate_planta, "categoria_her":cate_herramienta})
def cargarSuccess(request):
   
   return render(request, "success.html")

def cargarAbout(request):
   
   return render(request, "about.html")


def cargarContactanos(request):
   
   return render(request, "contactanos.html")
def cargarColabora(request):
   
   return render(request, "colabora.html")
def cargarEquipo(request):
   
   return render(request, "equipo.html")

def cargarAgregarUsuario(request):
    generos  = Genero.objects.all()
   
    return render(request,"registro.html", {"gen":generos})

   
def agregarUsuario(request):
    if request.method == 'POST':
        v_username = request.POST['txtusername']
        v_nombre = request.POST['txtnombre']
        v_appaterno = request.POST['txtappaterno']
        v_apmaterno = request.POST['txtapmaterno']
        v_rut = request.POST['txtrut']
        v_correo = request.POST['txtcorreo']
        v_telefono = request.POST['txttelefono']
        v_celular = request.POST['txtcelular']
        v_contraseña = request.POST['txtPass1']
        v_direccion = request.POST['txtdireccion']
        v_numero = request.POST['txtnumero']
        v_depto = request.POST['txtdepto']
        v_region = request.POST['txtregion']
        v_ciudad = request.POST['txtciudad']
        v_comuna = request.POST['txtcomuna']
        v_img = request.FILES.get('txtImg')

        genero_id = request.POST['cmbGenero']
    
        Usuario.objects.create(
            username = v_username,
            nombre=v_nombre,
            appaterno=v_appaterno,
            apmaterno=v_apmaterno,
            rut=v_rut,
            genero_id=genero_id,
            correo=v_correo,
            telefono=v_telefono,
            celular=v_celular,
            contraseña=v_contraseña,
            direccion=v_direccion,
            numero=v_numero,
            depto=v_depto,
            region=v_region,
            ciudad=v_ciudad,
            comuna=v_comuna,
            img_perf=v_img
        )

        return redirect('/success')

    




@login_required(login_url='login')  
def cargarEditarUsuario(request, id):
    usuario = Usuario.objects.get(rut=id)
    generos = Genero.objects.all()
    
    generoId = usuario.genero
    usuarioGeneroId = usuario.genero
    
    return render(request, "mi_cuenta.html", {"usu": usuario, "gen": generos, "generoId": usuarioGeneroId})

@login_required(login_url='login')
def editarUsuario(request):
    v_nombre = request.POST['txtnombre']
    v_rut = request.POST['txtrut']
    usuarioBD = Usuario.objects.get(rut=v_rut)
    v_appaterno = request.POST['txtappaterno']
    v_apmaterno = request.POST['txtapmaterno']
    v_correo = request.POST['txtcorreo']
    v_telefono = request.POST['txttelefono']
    v_celular = request.POST['txtcelular']
    v_contraseña = request.POST['txtPass1']
    v_direccion = request.POST['txtdireccion']
    v_numero = request.POST['txtnumero']
    v_depto = request.POST['txtdepto']
    v_region = request.POST['txtregion']
    v_ciudad = request.POST['txtciudad']
    v_comuna = request.POST['txtcomuna']
    v_img = request.FILES.get('txtImg')
    v_genero = Genero.objects.filter(nombre_genero=request.POST['cmbGenero']).first()


    try:
        v_img = request.FILES['txtImg']
        ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(usuarioBD.img_perf))
        os.remove(ruta_imagen)
    except:
        v_img = usuarioBD.img_perf

    usuarioBD.nombre = v_nombre 
    usuarioBD.appaterno = v_appaterno
    usuarioBD.apmaterno = v_apmaterno 
    usuarioBD.correo = v_correo
    usuarioBD.telefono = v_telefono 
    usuarioBD.celular = v_celular 
    usuarioBD.contraseña = v_contraseña 
    usuarioBD.direccion = v_direccion
    usuarioBD.numero = v_numero 
    usuarioBD.depto = v_depto 
    usuarioBD.region = v_region 
    usuarioBD.ciudad = v_ciudad 
    usuarioBD.comuna = v_comuna 
    usuarioBD.genero = v_genero    
    usuarioBD.img_perf = v_img 

    usuarioBD.save()

    return redirect('/success')




@login_required(login_url='login')
def cargarAgregarProducto(request):
    categorias  = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request,"agregarProductos.html", {"cate":categorias, "prod":productos})


@login_required(login_url='login')
def agregarProductos(request):
    print(request.POST)
    v_sku = request.POST['txtSku']
    v_nombre = request.POST['txtNombre']
    v_precio = request.POST['txtPrecio']
    v_stock = request.POST['txtStock']
    v_descripcion = request.POST['txtDescripcion']
    v_img = request.FILES['txtImg']
    
    
    categoria = Categoria.objects.get(id_categoria = request.POST['cmbCategoria'])
    
    Producto.objects.create(
        id_producto = v_sku , 
        nombre = v_nombre , 
        precio = v_precio, 
        stock = v_stock,
        descripcion = v_descripcion,
        img_url = v_img, 
        categoria_id = categoria)


    return redirect('/agregarProductos')


@login_required(login_url='login')
def cargarEditarProducto(request,id):

    producto = Producto.objects.get(id_producto = id)
    categorias = Categoria.objects.all()

    categoriaId = producto.categoria_id

    productoCategoriaId = Categoria.objects.get(id_categoria = categoriaId.id_categoria).id_categoria

    return render(request, "editarProducto.html",{"prod":producto,"cate":categorias,"categoriaId":productoCategoriaId})






@login_required(login_url='login')
def editarProducto(request):

    v_sku = request.POST['txtSku']
    productoBD = Producto.objects.get(id_producto = v_sku)
    v_nombre = request.POST['txtNombre']
    v_precio = request.POST['txtPrecio']
    v_stock = request.POST['txtStock']
    v_descripcion = request.POST['txtDescripcion']
   
    v_categoria = Categoria.objects.get(id_categoria = request.POST['cmbCategoria'])

    try:
        v_img = request.FILES['txtImg']
        ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(productoBD.img_url))
        os.remove(ruta_imagen)
        #delete 
    except:
        v_img = productoBD.img_url

    productoBD.nombre = v_nombre
    productoBD.precio = v_precio
    productoBD.stock = v_stock
    productoBD.descripcion = v_descripcion
    productoBD.categoria_id = v_categoria
    productoBD.img_url = v_img

    productoBD.save()

    return redirect('/agregarProductos')

@login_required(login_url='login')  
def eliminarProductos(request,id):

    producto = Producto.objects.get(id_producto = id)
    producto.delete()
    ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(producto.img_url))
    os.remove(ruta_imagen)

    return redirect('/agregarProductos')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/index')
        else:
            error_message = 'Credenciales inválidas. Inténtalo nuevamente.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
    

def catalogo(request):
    productos = Producto.objects.all()
    productos = Producto.objects.filter(stock__gt=0)
    return render(request, "catalogo.html", {'productos': productos})

@login_required(login_url='login')
def agregar_producto(request, id_producto):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=id_producto)
    carrito.agregar(producto)
    return redirect("catalogo")

@login_required(login_url='login')
def eliminar_producto(request, id_producto):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=id_producto)
    carrito.eliminar(producto)
    return redirect("catalogo")

@login_required(login_url='login')
def restar_producto(request, id_producto):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=id_producto)
    carrito.restar(producto)
    return redirect("catalogo")
@login_required(login_url='login') 
def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("catalogo")

user = Usuario.objects.get(username='fcojav')

# Otorga los permisos de administrador
user.is_staff = True
user.is_superuser = True
user.save()