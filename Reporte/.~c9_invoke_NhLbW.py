from django.shortcuts import render_to_response,render
from django.template import RequestContext
from Vents.models import VentaRegistrada
from datetime import *
from Usuario.models import *
from Producto.models import *
# Create your views here.



#Reportes textuales

def ventas_mes(request):
    
    ganancias_meses = [0,0,0,0,0,0,0,0,0,0,0,0]
    
    ventas = VentaRegistrada.objects.all()
    print ventas
    
    for venta in ventas:
        mes = venta.fecha.month
        ganancias_meses[int(mes)-1] = ganancias_meses[int(mes)-1] + venta.precioFinal
        
    # context = {
    #     "enero" : ganancias_meses[0],
    #     "febrero" : ganancias_meses[1],
    #     "marzo" : ganancias_meses[2],
    #     "abril" : ganancias_meses[3],
    #     "mayo" : ganancias_meses[4],
    #     "junio" : ganancias_meses[5],
    #     "julio" : ganancias_meses[6],
    #     "agosto" : ganancias_meses[7],
    #     "septiembre" : ganancias_meses[8],
    #     "octubre" : ganancias_meses[9],
    #     "noviembre" : ganancias_meses[10],
    #     "diciembre" : ganancias_meses[11],
    # }    
    
    print "Mayo"
    print ganancias_meses[4]
    if re
    if request.POST:
        
        p
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

        
    return render_to_response('ventas_mes_grafico.html',{},
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
    
    
    context = {
        "dias" : dias
    }
    
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
            
    return render_to_response('toppings_mas_vendidas.html',context,
	        		context_instance=RequestContext(request))


def sacar_minimo(diccionario, num_max):
    
    resultado = {}
    
    for x in range(0, num_max):
        key = min(diccionario, key=lambda i: diccionario[i])
        resultado[key] = diccionario[key]
        diccionario[key] = 10000000000
        
        
    return resultado