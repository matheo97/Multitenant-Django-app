# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.views.generic import TemplateView
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
import  simplejson
from .models import Producto
from .models import Topping
from pizzeria import settings 

# Create your views here.
class ListarTopping(TemplateView):
    def get(self,request,*args,**kwargs):
        try:
            toppings = Topping.objects.all()
            toppingsL = len(toppings)
        except:
            toppings = []
            toppingsL = 0
        context = {'toppings': toppings, 'toppingsL': toppingsL  } 
        return render_to_response(
            'listar_topping.html',
            context,
            context_instance=RequestContext(request))
            
    def post(self,request,*args,**kwargs):
		if "codigoTopping" in request.POST:
			try:
			    topping_codigo = request.POST['codigoTopping']
			    p = Topping.objects.get(codigo=topping_codigo)
			    mensaje = {'status':'True','codigoTopping':p.codigo}
			    p.delete()				
			except:
				mensaje = {'status':'False'} 
			response = simplejson.dumps(mensaje)
			return HttpResponse(response ,content_type='application/json')

class ListarProducto(TemplateView):
    def get(self,request,*args,**kwargs):
        try:
            productos = Producto.objects.all()
            pro=[]
            for i in productos:
            	nombre=i.imagen
            	toppings = i.toppings.all()
            	dic={'producto':i,'toppings':toppings}
            	pro.append(dic)
            productosL = len(productos)
        except:
            productos = []
            productosL = 0
            pro=[]
        context = {'productos': productos, 'productosL': productosL, 'pro':pro  } 
        return render_to_response(
            'listar_producto.html',
            context,
            context_instance=RequestContext(request))
            
    def post(self,request,*args,**kwargs):
		if "codigoProducto" in request.POST:
			try:
			    producto_codigo = request.POST['codigoProducto']
			    p = Producto.objects.get(referencia=producto_codigo)
			    mensaje = {'status':'True','codigoProducto':p.referencia}
			    p.delete()				
			except:
				mensaje = {'status':'False'} 
			response = simplejson.dumps(mensaje)
			return HttpResponse(response ,content_type='application/json')
    
def algo(request):
    return render_to_response('algo.html',context_instance=RequestContext(request))

class CrearProducto(TemplateView):
    
    def get(self,request,*args,**kwargs):
    	try:
            toppings = Topping.objects.all()
            toppingsL = len(toppings)
        except:
            toppings = []
            toppingsL = 0
        context = {'toppings': toppings, 'toppingsL': toppingsL  } 
        return render_to_response('crear_producto.html',context,
			context_instance=RequestContext(request))
			
    def post(self,request,*args,**kwargs):
        
        print request.POST
        referencia = request.POST['referencia']
        nombre = request.POST['nombre']
        porciones = request.POST['porciones']
        precio = request.POST['precio']
        descripcion = request.POST['descripcion']
        try
            imagen= request.FILES['imagen']
        except: 
            imagen = None
        toppings = request.POST.getlist('toppings')
        nameimazgen =settings.MEDIA_ROOT+"/"+str(imagen)
        	
        try:
            producto = Producto.objects.get(referencia=referencia)
            mensaje = "ya existe el producto"
            messages.info(request,mensaje)
            
            try:
                toppings = Topping.objects.all()
                toppingsL = len(toppings)
            except:
                toppings = []
                toppingsL = 0
            context = {'toppings': toppings, 'toppingsL': toppingsL  } 
            return render_to_response('crear_producto.html',context,
    			context_instance=RequestContext(request))
            
        except:
            
            producto = Producto(referencia=referencia, nombre=nombre,  imagen = imagen, height_field=30, width_field=30, numeroPorciones=porciones, precioBase=precio, descripcion=descripcion)
            producto.save()
            for i in toppings:
                topping= Topping.objects.get(codigo=i)
                producto.toppings.add(topping)
                
            mensaje = "El producto se registro con exito"
            messages.info(request,mensaje)
            
            try:
                productos = Producto.objects.all()
                pro=[]
                for i in productos:
                    toppings = i.toppings.all()
                    dic={'producto':i,'toppings':toppings}
                    pro.append(dic)
                productosL = len(productos)
            except:
                productos = []                
                productosL = 0
                pro=[]
            context = {'productos': productos, 'productosL': productosL, 'pro':pro  } 
            return render_to_response(
                'listar_producto.html',
                context,
                context_instance=RequestContext(request))
			
class CrearTopping(TemplateView):
    
    def get(self,request,*args,**kwargs):
		return render_to_response('crear_topping.html',
			context_instance=RequestContext(request))
			
    def post(self,request,*args,**kwargs):
        
        mensaje = ""
        try:
            descripcion=request.POST['descripcion']
            precio=     request.POST['precio']
            codigo=     request.POST['codigo']
            nombre=     request.POST['nombre']
            
            try:
				topping = Topping.objects.get(codigo=codigo)
				messages.info(request,"El topping con código "+str(codigo)+" ya existe.")
            
            except:
                topping = Topping (descripcion=descripcion, precio=precio, codigo=codigo, nombre=nombre)
                topping.save()
                mensaje = "Se creo el Topping"	
                try:
                    toppings = Topping.objects.all()
                    toppingsL = len(toppings)
                except:
                    toppings = []
                    toppingsL = 0
                messages.info(request,mensaje)
                context = {'toppings': toppings, 'toppingsL': toppingsL  }
                return render_to_response('listar_topping.html',context,context_instance=RequestContext(request))
            
        except: 	
			mensaje = "Debe llenar todos los campos"
			
        messages.info(request,mensaje)	
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
        
class EditarToppig(TemplateView):
    
	def get(self,request,*args,**kwargs):
		codigo = args[0]
		topping = Topping.objects.get(codigo=codigo)
		context={'topping':topping}
		return render_to_response('editar_topping.html',context,context_instance=RequestContext(request))
	
	def post(self,request,*args,**kwargs):
	    mensaje = ""
	    try:
	        descripcion = request.POST["descripcion"]
	        codigo      = request.POST["codigo"]
	        precio      = request.POST["precio"]
	        nombre      = request.POST["nombre"]
	        
	        topping = Topping.objects.get(codigo=codigo)
	        topping.nombre = nombre
	        topping.precio = precio
	        topping.descripcion = descripcion
	        topping.save()
	        mensaje = "Se ha editado con exito"
	    except Exception, e:
	        mensaje = "Ha ocurrido un error"
	    messages.info(request,mensaje)
	    try:
	        toppings = Topping.objects.all()
	        toppingsL = len(toppings)
	    except:
	        toppings = []
	        toppingsL = 0
	    context = {'toppings': toppings, 'toppingsL': toppingsL  }
	    return render_to_response('listar_topping.html',context,
			context_instance=RequestContext(request))


class EditarProducto(TemplateView):
    def get(self,request,*args,**kwargs):
		referencia = args[0]
		producto = Producto.objects.get(referencia=referencia)
		toppings = producto.toppings.all()
		toppings2 = Topping.objects.all()
		toppings3 = []
		for i in toppings2:
		    opcion = True
		    for e in toppings:
		        if i.codigo == e.codigo:
		            opcion = False
		    if opcion:
		        toppings3.append(i)
		        
		context={'producto':producto, 'toppings':toppings, 'toppings3':toppings3}
		return render_to_response('editar_producto.html',context,context_instance=RequestContext(request))
    
    def post(self,request,*args,**kwargs):
        """docstring for akjfklajdfhlkjadsf"""
        mensaje = ""
        try:
            descripcion = request.POST["descripcion"]
            referencia      = request.POST["referencia"]
            precio      = request.POST["precio"]
            nombre      = request.POST["nombre"]
            porciones   = request.POST["porciones"]
            topping = request.POST.getlist('toppings')
            
            
            producto = Producto.objects.get(referencia=referencia)
            producto.nombre = nombre
            producto.precioBase = precio
            producto.descripcion = descripcion
            producto.numeroPorciones = porciones
            try:
                imagen= request.FILES['imagen']
                producto.imagen=imagen
            except:
                pass
            producto.save()
            for i in producto.toppings.all():
                producto.toppings.remove(i)
            print "----------------------------------------------------------------------------------------------------"
            for i in topping:
                topping= Topping.objects.get(codigo=i)
                producto.toppings.add(topping)
            mensaje = "Se ha editado con exito"
        except Exception, e:
            mensaje = "Ha ocurrido un error"
            print e
        messages.info(request,mensaje)
        try:
            productos = Producto.objects.all()
            pro=[]
            for i in productos:
            	toppings = i.toppings.all()
            	dic={'producto':i,'toppings':toppings}
            	pro.append(dic)
            productosL = len(productos)
        except:
            productos = []
            productosL = 0
            pro=[]
        context = {'productos': productos, 'productosL': productosL, 'pro':pro  } 
        return render_to_response(
            'listar_producto.html',
            context,
            context_instance=RequestContext(request))

        
        # TODO: write code...
    
	

