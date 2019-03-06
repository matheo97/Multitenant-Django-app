# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.views.generic import TemplateView
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from .models import Producto
from .models import Topping

# Create your views here.

class CrearProducto(TemplateView):
    
    def get(self,request,*args,**kwargs):
		return render_to_response('crear_producto.html',
			context_instance=RequestContext(request))
			
    def post(self,request,*args,**kwargs):
    
        referencia = request.POST['referencia']
        nombre = request.POST['nombre']
        porciones = request.POST['porciones']
        precio = request.POST['precio']
        descripcion = request.POST['descripcion']
        
        try:
            producto = Producto(nombre = nombre, referencia=referencia, descripcion = descripcion, numeroPorciones=porciones)
        except: 
	       print "crear_topping"
	       
class CrearTopping(TemplateView):
    
    def get(self,request,*args,**kwargs):
		return render_to_response('crear_topping.html',
			context_instance=RequestContext(request))
			
    def post(self,request,*args,**kwargs):
        
        try:
            descripcion=request.POST['descripcion']
            precio=     request.POST['precio']
            codigo=     request.POST['codigo']
        except:
            campoVacio(descripcion)
            campoVacio(precio)
            campoVacio(codigo)
            campoVacio(nombre)
            
            try:
				topping = Topping.objects.get(codigo=codigo)
				messages.info(request,"El topping con código "+str(codigo)+" ya existe.")
            
            except:
                topping = Topping (descripcion=descripcion, precio=precio, codigo=codigo, nombre=nombre)
            
        except: 	
			messages.info(request,"Debe llenar todos los campos")
			
			
			
        return render_to_response('crear_topping.html',
			context_instance=RequestContext(request))
			
def campoVacio(valor):
	vacio = True
	for i in valor:
		if i != " ":
			vacio = False	

	if vacio:	
		raise Error1("Debe proporcionar todos los campos ")
		
		
class Error1(Exception):
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return repr(self.valor)