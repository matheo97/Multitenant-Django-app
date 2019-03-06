# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response, render, get_object_or_404
from Tenant.models import Franquicia
from django.template import RequestContext
from django.views.generic import TemplateView
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages

from Tenant.models import Franquicia
from Tenant.models import Dominio
from Vents.models import VentaRegistrada
from django.db import connection
# Create your views here.

class Prueba(TemplateView):
    def get(self,request,*args,**kwargs):
        francs = VentaRegistrada.objects.all()
        for i in francs:
            print str(i)
        context = ""
        return render(request, "aux.html")