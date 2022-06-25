
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

from django.template import Template, context




def mi_template(request):
    
    archivo = open(r'C:\Users\garba\Desktop\EntregableClase19\MVT-JonatanFrean\templates\prueba.html', 'r')
    
    familia = familia(nombre = 'Carlos', edad = 20)
    
    template1 = Template(archivo.read())
    
    contexto1 = context()
    
    render1 = template1.render(contexto1)
    
    return HttpResponse(render1)