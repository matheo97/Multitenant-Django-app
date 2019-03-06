# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response, render, get_object_or_404
from Tenant.models import Franquicia
from django.template import RequestContext
from django.views.generic import TemplateView
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from Producto.models import Producto
from Producto.models import Topping
from .models import Elemento
from .models import Carrito
from .models import VentaRegistrada
from Usuario.models import Usuario
from django.contrib import messages

# Create your views here.
class Ventas(TemplateView):
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
            adiciones = Topping.objects.all()
        except:
            productos = []
            productosL = 0
            pro=[]
            adiciones = []
            
        subdominio = request.META['HTTP_HOST'].split('.')[0]
        franquicia = get_object_or_404(Franquicia, nombre=subdominio)
        
        color = franquicia.color
        nav_var_color = franquicia.nav_var_color
        sidebar_grid = franquicia.sidebar_grid
        tinte = franquicia.tinte
        font = franquicia.font
        
        context = {'productos': productos, 'productosL': productosL, 'pro':pro, 'adiciones':adiciones , 'black': tinte, 'grid' : sidebar_grid, 'inverse': nav_var_color, 'color' : color, 'font' : font } 
        return render_to_response(
            'lista_de_pizzas.html',
            context,
            context_instance=RequestContext(request))
            
    def post(self,request,*args,**kwargs):
        referencia = request.POST['referencia']
        toppings = request.POST.getlist('toppings')
        
        
        producto = Producto.objects.get(referencia=referencia)
        elemento = Elemento(pizza=producto)
        elemento.save()
        message = ""
        for i in toppings:
            topping = Topping.objects.get(codigo=i)
            elemento.toppings.add(topping)
        try:    
            id_user =  request.user.id
            usuario = Usuario.objects.get(id=id_user)
        except:
            id_user = 2
            usuario = Usuario.objects.get(id=id_user)
            message = "No estas registrado"
        
        print id_user    
        
        subtotal = 0
        canasta = Carrito.objects.get(usuario=usuario)
        canasta.pizza.add(elemento)
        canasta.save()
        for i in canasta.pizza.all():
            subtotal += i.pizza.precioBase
            for e in i.toppings.all():
                subtotal += e.precio
        total = 2000+subtotal
        
        option = False    
        context = {'carrito':canasta,'message':message, 'option':option, 'total':total, 'subtotal':subtotal}
       
        return render_to_response(
            'checkout.html',
            context,
            context_instance=RequestContext(request))

class RegistrarVenta(TemplateView):
    def post(self,request,*args,**kwargs):
        option = False
        nombre = request.POST['nombre']
        direccion  = request.POST['dir']
        tar = request.POST['tar']
        try:
            id_user =  request.user.id
            usuario = Usuario.objects.get(id=id_user)
            canasta = Carrito.objects.get(usuario=usuario)
            
        
        except:
            id_user = 2
            usuario = Usuario.objects.get(id=id_user)
            canasta = Carrito.objects.get(usuario=usuario)
            
        if len(canasta.pizza.all())>0:
            venta = VentaRegistrada(usuario=canasta.usuario, nombre=nombre, direccion=direccion, tarjeta=tar)
            venta.save()
                
            
            precio = 0
                
            
            for i in canasta.pizza.all():
                venta.pizza.add(i)
                precio += i.pizza.precioBase
                for e in i.toppings.all():
                    precio += e.precio
            
            sub = precio
            precio +=2000
            venta.precioFinal = precio
            venta.save()
                
            venta.save()
            canasta.pizza.clear()
            option = True    
            message = "Tu compra ha sido exitosa"
            
            messages.info(request,"Compra relalizada con exito, sigue comprando.")
        else:
            message = "No hay nada en tu carrito"

        context = {'carrito':canasta,'message':message, 'option':option, 'nombre':nombre, 'direccion':direccion, 'tarjeta':tar}
        return render_to_response(
            'checkout.html',
            context,
            context_instance=RequestContext(request))
        
        