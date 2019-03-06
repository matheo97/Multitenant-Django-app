from __future__ import unicode_literals

from django.db import models
from Producto.models import Producto
from Producto.models import Topping
from Usuario.models import Cliente
# Create your models here.

class Elemento(models.Model):
    pizza = models.ForeignKey(Producto,on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping)
    class Meta:
		db_table = 'Elemento'
    
class VentaRegistrada(models.Model):
    id_Venta = models.AutoField(primary_key=True)
    pizza = models.ManyToManyField(Elemento)
    usuario = models.ForeignKey(Cliente)
    nombre = models.CharField(max_length=100, null=True, default="")
    direccion = models.CharField(max_length=100, null=True, default="")
    tarjeta = models.CharField(max_length=100, null=True, default="")
    precioFinal= models.IntegerField(null=True,blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    precioFinal= models.IntegerField(null=True,blank=True)
    class Meta:
		db_table = 'VentaRegistrada'
		
    
class Carrito(models.Model):
    pizza = models.ManyToManyField(Elemento)
    usuario = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    class Meta:
		db_table = 'Carrito'

class Recibo(models.Model):
    doc = models.FileField(null=True,blank=True,upload_to='recibo/')
	 
    