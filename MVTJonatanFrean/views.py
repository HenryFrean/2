
from django.http import HttpResponse


def inicio(request):
    return HttpResponse('Hola')

def ver_fecha(request):
    return HttpResponse('Fecha actual: ')