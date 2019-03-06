from django.shortcuts import render_to_response,render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import *
import json
from Vents.models import VentaRegistrada
from Usuario.models import *
from Producto.models import *
from Tenant.models import Franquicia


def ventas_mes(request):
    
    ganancias_meses = [0,0,0,0,0,0,0,0,0,0,0,0]
    
    ventas = VentaRegistrada.objects.all()
    print ventas
    
    for venta in ventas:
        mes = venta.fecha.month
        ganancias_meses[int(mes)-1] = ganancias_meses[int(mes)-1] + venta.precioFinal
        
    context = {
        "enero" : ganancias_meses[0],
        "febrero" : ganancias_meses[1],
        "marzo" : ganancias_meses[2],
        "abril" : ganancias_meses[3],
        "mayo" : ganancias_meses[4],
        "junio" : ganancias_meses[5],
        "julio" : ganancias_meses[6],
        "agosto" : ganancias_meses[7],
        "septiembre" : ganancias_meses[8],
        "octubre" : ganancias_meses[9],
        "noviembre" : ganancias_meses[10],
        "diciembre" : ganancias_meses[11],
    }    
    
    print "Mayo"
    print ganancias_meses[4]
    
    if request.method == 'POST':
        
        print "entro veve"
        
        dicc={}
        dicc['enero'] = ganancias_meses[0]
        dicc['febrero'] = ganancias_meses[1]
        dicc['marzo'] = ganancias_meses[2]
        dicc['abril'] = ganancias_meses[3]
        dicc['mayo'] = ganancias_meses[4]
        dicc['junio'] = ganancias_meses[5]
        dicc['julio'] = ganancias_meses[6]
        dicc['agosto'] = ganancias_meses[7]
        dicc['septiembre'] = ganancias_meses[8]
        dicc['octubre'] = ganancias_meses[9]
        dicc['noviembre'] = ganancias_meses[10]
        dicc['diciembre'] = ganancias_meses[11]
        
        data=json.dumps(dicc)
        mimetype="application/json"
        
        
        return HttpResponse(data,mimetype)

    
    #Esto checkea si la franquicia tiene o no reportes graficos activos
    subdominio = request.META['HTTP_HOST'].split('.')[0]
    franquicia = get_object_or_404(Franquicia, nombre=subdominio)
    
    color = franquicia.color
    nav_var_color = franquicia.nav_var_color
    sidebar_grid = franquicia.sidebar_grid
    tinte = franquicia.tinte
    font = franquicia.font
    
    context['black'] = tinte
    context['grid'] = sidebar_grid
    context['inverse']= nav_var_color
    context['color'] = color
    context['font'] = font
    
    if franquicia.reportes_graficos == 'ACTIVO':
        return render_to_response('ventas_mes_grafico.html',context,
	        		context_instance=RequestContext(request))

    return render_to_response('ventas_mes.html',context,
	        		context_instance=RequestContext(request))

def registrados_mes(request):
    
    registrados_mes = [0,0,0,0,0,0,0,0,0,0,0,0]
    
    usuarios = Cliente.objects.all()
    
    for cliente in usuarios:
        mes = cliente.fecha_registro.month
        registrados_mes[int(mes)-1] = registrados_mes[int(mes)-1] + 1
        
    
    context = {
        "enero" : registrados_mes[0],
        "febrero" : registrados_mes[1],
        "marzo" : registrados_mes[2],
        "abril" : registrados_mes[3],
        "mayo" : registrados_mes[4],
        "junio" : registrados_mes[5],
        "julio" : registrados_mes[6],
        "agosto" : registrados_mes[7],
        "septiembre" : registrados_mes[8],
        "octubre" : registrados_mes[9],
        "noviembre" : registrados_mes[10],
        "diciembre" : registrados_mes[11],
    }
    
    
    if request.method == 'POST':
        
        print "entro veve"
        
        dicc={}
        dicc['enero'] = registrados_mes[0]
        dicc['febrero'] = registrados_mes[1]
        dicc['marzo'] = registrados_mes[2]
        dicc['abril'] = registrados_mes[3]
        dicc['mayo'] = registrados_mes[4]
        dicc['junio'] = registrados_mes[5]
        dicc['julio'] = registrados_mes[6]
        dicc['agosto'] = registrados_mes[7]
        dicc['septiembre'] = registrados_mes[8]
        dicc['octubre'] = registrados_mes[9]
        dicc['noviembre'] = registrados_mes[10]
        dicc['diciembre'] = registrados_mes[11]
        
        data=json.dumps(dicc)
        mimetype="application/json"
        
        
        return HttpResponse(data,mimetype)
        
        
    #Esto checkea si la franquicia tiene o no reportes graficos activos
    subdominio = request.META['HTTP_HOST'].split('.')[0]
    franquicia = get_object_or_404(Franquicia, nombre=subdominio)
    
    color = franquicia.color
    nav_var_color = franquicia.nav_var_color
    sidebar_grid = franquicia.sidebar_grid
    tinte = franquicia.tinte
    font = franquicia.font
    
    context['black'] = tinte
    context['grid'] = sidebar_grid
    context['inverse']= nav_var_color
    context['color'] = color
    context['font'] = font
    
    if franquicia.reportes_graficos == 'ACTIVO':
        return render_to_response('registrados_mes_grafico.html',context,
	        		context_instance=RequestContext(request))

    return render_to_response('registrados_mes.html',context,
	        		context_instance=RequestContext(request))
  
def pizzas_mas_vendidas(request):
    
    ventas = VentaRegistrada.objects.all()
    pizzas = Producto.objects.all()
    pizzas_vendidas = {}
    
    for pizza in pizzas:
        pizzas_vendidas[pizza.referencia] = 0
    
    for venta in ventas:
        elementos = venta.pizza
        
        for elemento in elementos.all():
            pizza = elemento.pizza.referencia
            pizzas_vendidas[pizza] = pizzas_vendidas[pizza] + 1 
    
    print pizzas_vendidas
    pizzas_vendidas = sacar_maximo(pizzas_vendidas, 3)
    
    context = {
        "pizzas_vendidas" : pizzas_vendidas
    }
    
    print pizzas_vendidas
    
    if request.method == 'POST':
        
        print "entro veve"
        
        dicc={}
        dicc['valor1'] = pizzas_vendidas.values()[0]
        dicc['valor2'] = pizzas_vendidas.values()[1]
        dicc['valor3'] = pizzas_vendidas.values()[2]
        dicc['referencia1'] = pizzas_vendidas.keys()[0]
        dicc['referencia2'] = pizzas_vendidas.keys()[1]
        dicc['referencia3'] = pizzas_vendidas.keys()[2]
        
        print "Este es el dicc"
        print dicc
        data=json.dumps(dicc)
        mimetype="application/json"
        
        
        return HttpResponse(data,mimetype)
        
    #Esto checkea si la franquicia tiene o no reportes graficos activos
    subdominio = request.META['HTTP_HOST'].split('.')[0]
    franquicia = get_object_or_404(Franquicia, nombre=subdominio)
    
    color = franquicia.color
    nav_var_color = franquicia.nav_var_color
    sidebar_grid = franquicia.sidebar_grid
    tinte = franquicia.tinte
    font = franquicia.font
    
    context['black'] = tinte
    context['grid'] = sidebar_grid
    context['inverse']= nav_var_color
    context['color'] = color
    context['font'] = font
    
    if franquicia.reportes_graficos == 'ACTIVO':
        return render_to_response('pizzas_mas_vendidas_grafico.html',context,
	        		context_instance=RequestContext(request))
        
    return render_to_response('pizzas_mas_vendidas.html',context,
	        		context_instance=RequestContext(request))
	        		
def toppings_mas_vendidos(request):
    
    ventas = VentaRegistrada.objects.all()
    toppings = Topping.objects.all()
    toppings_vendidas = {}
    
    for topping in toppings:
        toppings_vendidas[topping.codigo] = 0
    
    for venta in ventas:
        elementos = venta.pizza
        
        for elemento in elementos.all():
            toppings = elemento.toppings
            
            for topping in toppings.all():
                top = topping.codigo
                toppings_vendidas[top] = toppings_vendidas[top] + 1 
    
    print toppings_vendidas
    toppings_vendidas = sacar_maximo(toppings_vendidas, 3)
    
    context = {
        "toppings_vendidas" : toppings_vendidas
    }
    
    if request.method == 'POST':
        
        print "entro veve"
        
        dicc={}
        dicc['valor1'] = toppings_vendidas.values()[0]
        dicc['valor2'] = toppings_vendidas.values()[1]
        dicc['valor3'] = toppings_vendidas.values()[2]
        dicc['referencia1'] = toppings_vendidas.keys()[0]
        dicc['referencia2'] = toppings_vendidas.keys()[1]
        dicc['referencia3'] = toppings_vendidas.keys()[2]
        
        print "Este es el dicc"
        print dicc
        data=json.dumps(dicc)
        mimetype="application/json"
        
        
        return HttpResponse(data,mimetype)
        
        
    #Esto checkea si la franquicia tiene o no reportes graficos activos
    subdominio = request.META['HTTP_HOST'].split('.')[0]
    franquicia = get_object_or_404(Franquicia, nombre=subdominio)
    
    color = franquicia.color
    nav_var_color = franquicia.nav_var_color
    sidebar_grid = franquicia.sidebar_grid
    tinte = franquicia.tinte
    font = franquicia.font
    
    context['black'] = tinte
    context['grid'] = sidebar_grid
    context['inverse']= nav_var_color
    context['color'] = color
    context['font'] = font
    
    if franquicia.reportes_graficos == 'ACTIVO':
        return render_to_response('toppings_mas_vendidas_grafico.html',context,
	        		context_instance=RequestContext(request))
            
    return render_to_response('toppings_mas_vendidas.html',context,
	        		context_instance=RequestContext(request))
    
def sacar_maximo(diccionario, num_max):
    
    resultado = {}
    
    for x in range(0, num_max):
        key = max(diccionario, key=lambda i: diccionario[i])
        resultado[key] = diccionario[key]
        diccionario[key] = 0
        
        
    return resultado
        
def dias_mas_ventas(request):
    
    dias = {}
    
    dias["lunes"] = 0
    dias["martes"] = 0
    dias["miercoles"] = 0
    dias["jueves"] = 0
    dias["viernes"] = 0
    dias["sabado"] = 0
    dias["domingo"] = 0
    
    lunes = VentaRegistrada.objects.filter(fecha__week_day=2)
    martes = VentaRegistrada.objects.filter(fecha__week_day=3)
    miercoles = VentaRegistrada.objects.filter(fecha__week_day=4)
    jueves = VentaRegistrada.objects.filter(fecha__week_day=5)
    viernes = VentaRegistrada.objects.filter(fecha__week_day=6)
    sabado = VentaRegistrada.objects.filter(fecha__week_day=7)
    domingo = VentaRegistrada.objects.filter(fecha__week_day=1)
    
    for venta in lunes:
        dias["lunes"] = dias["lunes"] + venta.precioFinal
    
    for venta in martes:
        dias["martes"] = dias["martes"] + venta.precioFinal
    
    for venta in miercoles:
        dias["miercoles"] = dias["miercoles"] + venta.precioFinal
        
    for venta in jueves:
        dias["jueves"] = dias["jueves"] + venta.precioFinal
    
    for venta in viernes:
        dias["viernes"] = dias["viernes"] + venta.precioFinal
    
    for venta in sabado:
        dias["sabado"] = dias["sabado"] + venta.precioFinal
        
    for venta in domingo:
        dias["domingo"] = dias["domingo"] + venta.precioFinal
        
    
    if request.method == 'POST':
        
        print "entro veve"
        
        dicc={}
        dicc['lunes'] = dias["lunes"]
        dicc['martes'] = dias["martes"]
        dicc['miercoles'] = dias["miercoles"]
        dicc['jueves'] = dias["jueves"]
        dicc['viernes'] = dias["viernes"]
        dicc['sabado'] = dias["sabado"]
        dicc['domingo'] = dias["domingo"]
        
        data=json.dumps(dicc)
        mimetype="application/json"
        
        
        return HttpResponse(data,mimetype)
    context = {
        "dias" : dias
    }
    
    
    #Esto checkea si la franquicia tiene o no reportes graficos activos
    subdominio = request.META['HTTP_HOST'].split('.')[0]
    franquicia = get_object_or_404(Franquicia, nombre=subdominio)
    
    color = franquicia.color
    nav_var_color = franquicia.nav_var_color
    sidebar_grid = franquicia.sidebar_grid
    tinte = franquicia.tinte
    font = franquicia.font
    
    context['black'] = tinte
    context['grid'] = sidebar_grid
    context['inverse']= nav_var_color
    context['color'] = color
    context['font'] = font
    
    if franquicia.reportes_graficos == 'ACTIVO':
        return render_to_response('dias_mas_ventas_grafico.html',context,
    	        		context_instance=RequestContext(request))
    	        		
    
    return render_to_response('dias_mas_ventas.html',context,
    	        		context_instance=RequestContext(request))
	        		
def toppings_menos_vendidos(request):
    
    ventas = VentaRegistrada.objects.all()
    toppings = Topping.objects.all()
    toppings_vendidas = {}
    
    for topping in toppings:
        toppings_vendidas[topping.codigo] = 0
    
    for venta in ventas:
        elementos = venta.pizza
        
        for elemento in elementos.all():
            toppings = elemento.toppings
            
            for topping in toppings.all():
                top = topping.codigo
                toppings_vendidas[top] = toppings_vendidas[top] + 1 
    
    print toppings_vendidas
    toppings_vendidas = sacar_minimo(toppings_vendidas, 3)
    
    context = {
        "toppings_vendidas" : toppings_vendidas
    }
    
    if request.method == 'POST':
        
        print "entro veve"
        
        dicc={}
        dicc['valor1'] = toppings_vendidas.values()[0]
        dicc['valor2'] = toppings_vendidas.values()[1]
        dicc['valor3'] = toppings_vendidas.values()[2]
        dicc['referencia1'] = toppings_vendidas.keys()[0]
        dicc['referencia2'] = toppings_vendidas.keys()[1]
        dicc['referencia3'] = toppings_vendidas.keys()[2]
        
        print "Este es el dicc"
        print dicc
        data=json.dumps(dicc)
        mimetype="application/json"
        
        
        return HttpResponse(data,mimetype)
        
    
    #Esto checkea si la franquicia tiene o no reportes graficos activos
    subdominio = request.META['HTTP_HOST'].split('.')[0]
    franquicia = get_object_or_404(Franquicia, nombre=subdominio)
    
    color = franquicia.color
    nav_var_color = franquicia.nav_var_color
    sidebar_grid = franquicia.sidebar_grid
    tinte = franquicia.tinte
    font = franquicia.font
    
    context['black'] = tinte
    context['grid'] = sidebar_grid
    context['inverse']= nav_var_color
    context['color'] = color
    context['font'] = font
    
    if franquicia.reportes_graficos == 'ACTIVO':
        return render_to_response('toppings_mas_vendidas_grafico.html',context,
	        		context_instance=RequestContext(request))
            
    return render_to_response('toppings_mas_vendidas.html',context,
	        		context_instance=RequestContext(request))
	        		
def sacar_minimo(diccionario, num_max):
    
    resultado = {}
    
    for x in range(0, num_max):
        key = min(diccionario, key=lambda i: diccionario[i])
        resultado[key] = diccionario[key]
        diccionario[key] = 10000000000
        
        
    return resultado