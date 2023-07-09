from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import *


class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
    
    def agregar(self, producto):
        id = str(producto.id_producto)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "id_producto": producto.id_producto,
                "nombre": producto.nombre,
                "acumulado": producto.precio,
                "cantidad": 1,
            }
        else: 
            self.carrito[id]["cantidad"] +=1
            self.carrito[id]["acumulado"] += producto.precio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id=str(producto.id_producto)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar(self, producto):
        id = str(producto.id_producto)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.precio
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

    def comprar_producto(request, producto_id, cantidad):
        producto = get_object_or_404(Producto, id_producto=producto_id)

        if producto.stock >= cantidad:
            producto.stock -= cantidad
            producto.save()
            

            return HttpResponse("Compra realizada exitosamente.")
        else:
            return HttpResponse("No hay suficiente stock disponible.")        