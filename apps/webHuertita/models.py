from django.db import models

# Create your models here.
class Categorias(models.Model):
    cat_id = models.IntegerField(primary_key=True)
    cat_nombre = models.CharField(max_length=50,null=False)

    #Formateo
    def __str__(self):
        txt = "nombre: {0} - ID : {1}"
        return txt.format(self.cat_nombre,self.cat_id)



class Productos(models.Model):
    prod_id = models.IntegerField(primary_key=True)
    prod_nombre = models.CharField(max_length=50,null=False)
    prod_precio = models.IntegerField(null=False)
    cat_id = models.ForeignKey(Categorias,on_delete=models.CASCADE)
    prod_stock = models.IntegerField(null=False)
    prod_descripcion = models.CharField(max_length=150 ,null=False)
    prod_img_url = models.ImageField(upload_to='imagenesProducto')
    prod_fecha_inicio = models.DateField(auto_now_add=True)

    def __str__(self):
        txt = "Codigo: {0} - Nombre: {1} - Categoria: {2} -  fecha: {3}"
        return txt.format(self.prod_id, self.prod_nombre,self.cat_id ,self.prod_fecha_inicio)
    
class Usuarios(models.Model):
    rut = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50,null=False)
    appaterno = models.CharField(max_length=50,null=False)
    apmaterno = models.CharField(max_length=50,null=False)
    genero = models.CharField(max_length=20,null=False)
    correo = models.EmailField(max_length=80,null=False)
    telefono = models.IntegerField(null=False)
    celular = models.IntegerField(null=False)
    contraseña = models.CharField(max_length=30,null=False)
    direccion = models.CharField(max_length=50,null=False)
    numero = models.IntegerField(null=False)
    depto = models.CharField(max_length=6,null=False)
    region = models.CharField(max_length=60,null=False)
    ciudad = models.CharField(max_length=60,null=False)
    comuna = models.CharField(max_length=60,null=False)
    fecha_creacion = models.DateField(auto_now_add=True)
    

    def __str__(self):
        txt = "Rut: {0} - Nombre: {1} - Ap_paterno: {2} -  Ap_materno: {3} - Direccion {4} - Creacion {5} "
        return txt.format(self.rut, self.nombre,self.appaterno ,self.apmaterno, self.direccion,self.fecha_creacion)
    

class venta (models.Model):
    id_venta = models.IntegerField(primary_key=True)
    rut = models.ForeignKey(Usuarios,on_delete=models.CASCADE)
    prod_id = models.ForeignKey(Productos,on_delete=models.CASCADE)
    fecha_compra = models.DateField(auto_now_add=True)
    cantidad = models.IntegerField(null=False)


