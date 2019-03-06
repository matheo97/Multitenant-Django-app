from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.views.generic import TemplateView
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from Producto.models import Producto
from Producto.models import Topping
from .models import Elemento
from .models import Carrito
from Usuario.models import Usuario

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
        context = {'productos': productos, 'productosL': productosL, 'pro':pro, 'adiciones':adiciones  } 
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
        for i in toppings:
            topping = Topping.objects.get(codigo=i)
            elemento.toppings.add(topping)
            
        id_user =  request.user.id
        usuario = Usuario.objects.get(id=id_user)
        print "usuario ok --------------------------------------------------------------------------------------------------------------------------------------------------------------"
        
        canasta = Canasta.objects.get(usuario=usuario)
        print "canasta  ok --------------------------------------------------------------------------------------------------------------------------------------------------------------"
            
        
        
        
        productos = []
        productosL = 0
        pro=[]
        adiciones = []
        context = {'productos': productos, 'productosL': productosL, 'pro':pro, 'adiciones':adiciones  } 
        return render_to_response(
            'lista_de_pizzas.html',
            context,
            context_instance=RequestContext(request))
        