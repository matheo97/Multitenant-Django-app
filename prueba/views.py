from django.shortcuts import render

# Create your views here.
def prueba(request):
	prueba = "HOLA DJANGO"
	return render(request, "prueba.html", {
		"prueba": prueba,
	})