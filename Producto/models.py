from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Topping (models.Model):
    
    codigo = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=50,null=True,blank=True)
    descripcion = models.CharField(max_length=350,null=True,blank=True)
    precio = models.IntegerField(null=True,blank=True)
    class Meta:
		db_table = 'topping'
    

        
class Producto(models.Model):
    
    referencia = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=50,null=True,blank=True)
    descripcion = models.CharField(max_length=350,null=True,blank=True)
    numeroPorciones = models.IntegerField(null=True,blank=True)
    precioBase = models.IntegerField(null=True,blank=True)
    imagen = models.ImageField(null=True,blank=True,upload_to='img/pizzas/',width_field="width_field",height_field = "height_field")
    height_field= models.IntegerField(default=0)
    width_field= models.IntegerField(default=0) 
    
    toppings = models.ManyToManyField(Topping)
    class Meta:
		db_table = 'producto'