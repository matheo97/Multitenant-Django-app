import logging
import logging.config
from Usuario.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login
from django.test import RequestFactory
from django.contrib import messages
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@csrf_exempt
def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        
        try:
            cliente = Usuario.objects.get(username = kwargs['details']['email'])
        except:
            cliente = None
           
        
        request_factory = RequestFactory()
        request1 = request_factory.get('/path', data={'user': cliente, 'COOKIES': "ADSA"})
        
        if cliente is None:
            usuario = {
                'email' : kwargs['details']['email'],
                'nombre' : kwargs['details']['first_name'],
                'apellido' : kwargs['details']['last_name']
            }
            return render(request1, 'formulario_crear_cliente_landing.html', {'Autenticado':'No', 'usuario' : usuario})
        else:
            return {'user' : cliente}
        
# # facebook.py
# def check_registered(*args, **kwargs):
#     ''' check that the user completed the registration form '''
#     log.info('check if user registered')
#     request = kwargs.get('request')
#     has_registered = request.session.get('register_data')
#     if has_registered:
#         log.info('user registration complete')
#         return None
        
#     return redirect('register')
#     #return HttpResponseRedirect(reverse("usuario:register"))


# def check_profile(*args, **kwargs):
#     ''' check that the user have an existing profile '''
#     log.info('check if user profile exists')
#     request = kwargs.get('request')
#     customer_data = request.session.get('register_data')
#     print "Esta es la data traida del Face"
#     print customer_data
#     cliente, is_new = Cliente.objects.get_or_create(user=kwargs.get('user'), defaults=customer_data)
#     return {
#         'customer':cliente
#     }
    

# class RegisterForm(forms.ModelForm):
#     ''' simple ModelForm with some additionnal fields (birthdate, gender, city...) '''
#     class Meta:
#         model = Cliente
#         exclude = ('user',)

    
# def register_form(request):
#     ''' when not registered, user is redirected to this form '''
#     request.session['register_data'] = False
#     pipeline_session_key = setting('SOCIAL_AUTH_PARTIAL_PIPELINE_KEY', 'partial_pipeline')
#     form = None
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             # form is valid, go next step
#             request.session['register_data'] = form.cleaned_data 
#             backend = request.session[pipeline_session_key]['backend']
#             return redirect('socialauth_complete', backend=backend)

#     template_data = {}

#     if not form:
#         # initiate form with facebook values if any
#         user_data = request.session.get(pipeline_session_key, {}).get('kwargs', {}).get('response', {})
#         if not user_data:
#              return redirect('socialauth_complete', backend=backend)
#         initial_values = {
#             'email': user_data.get('email'),
#             'first_name': user_data.get('first_name'),
#             'last_name': user_data.get('last_name'),
#             'city': user_data.get('location', {}).get('name', '').split(',')[0],
#             'birthdate': user_data.get('birthday'),
#             'gender': 'Mme' if user_data.get('gender') == 'female' else 'M',
#         }
#         template_data['form_values'] = initial_values
#         form = RegisterForm(initial=initial_values)

#     tpl = Template('''
#         <form action="" method="POST">
#             {% csrf_token %}
#             <p>
#                 {{ form.as_ul }}
#             </p>
#             <input type="submit" value="Send" />
#         </form>''')

#     template_data['form'] = form

#     return HttpResponse(tpl.render(RequestContext(request, template_data)))