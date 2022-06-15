from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Familia

# Create your views here.
def familia(self):

    familia=Familia(nombre="Juan",apellido="Camacho",bd="1975/01/06",edad=47 )
    familia.save()
    documento =f"El nombre del familiar es : {familia.nombre}, de apellido{familia.apellido} nacido el dia {familia.FC} con una edad de {familia.edad}"
    return HttpResponse(documento)