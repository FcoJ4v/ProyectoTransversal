from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50, null=False)

    def __str__(self):
        txt = "nombre: {0} - ID : {1}"
        return txt.format(self.nombre_categoria, self.id_categoria)


class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    precio = models.IntegerField(null=False)
    categoria_id = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    stock = models.IntegerField(null=False)
    descripcion = models.CharField(max_length=150, null=False)
    img_url = models.ImageField(upload_to='imagenesProducto')
    fecha_agregar = models.DateField(auto_now_add=True)

    def __str__(self):
        txt = "Codigo: {0} - Nombre: {1} - Categoria: {2} - fecha: {3}"
        return txt.format(self.id_producto, self.nombre, self.categoria_id, self.fecha_agregar)


class Genero(models.Model):
    id_genero = models.IntegerField(primary_key=True, null=False)
    nombre_genero = models.CharField(max_length=50, null=False)

    def __str__(self):
        txt = "ID: {0} - Genero: {1}"
        return txt.format(self.id_genero, self.nombre_genero)


class Usuario(AbstractUser):
    username = models.CharField(max_length=15, null=False)
    rut = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50, null=True)
    appaterno = models.CharField(max_length=50, null=True)
    apmaterno = models.CharField(max_length=50, null=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE,max_length=50, null=True)
    correo = models.EmailField(max_length=80, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    celular = models.IntegerField(blank=True, null=True)
    contraseña = models.CharField(max_length=30, null=False)
    direccion = models.CharField(max_length=50, null=False)
    numero = models.IntegerField(blank=True, null=True)
    depto = models.IntegerField(blank=True, null=True)
    region = models.CharField(max_length=60, blank=True, null=True)
    ciudad = models.CharField(max_length=60, blank=True, null=True)
    comuna = models.CharField(max_length=60,blank=True, null=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    img_perf = models.ImageField(upload_to='imagenesPerfiles')
    

    def __str__(self):
        txt = "Rut: {0} - Nombre: {1} - Ap_paterno: {2} - Ap_materno: {3} - Direccion: {4} - Creacion: {5}"
        return txt.format(self.rut, self.nombre, self.appaterno, self.apmaterno, self.direccion, self.fecha_creacion)
    
@receiver(post_save, sender=Usuario)
def assign_user_to_group(sender, instance, created, **kwargs):
        if created:
            group = Group.objects.get(name='Clientes')
            instance.groups.add(group)


Group.objects.get_or_create(name='Administradores')
Group.objects.get_or_create(name='Clientes')

   