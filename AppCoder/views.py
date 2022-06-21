from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Familia

# Create your views here.
def familiar1(self):

    familiar1=Familia(nombre="Juan",apellido="Camacho",bd="1975-01-06",edad=47 )
    familiar1.save()
    documento =f"El nombre del familiar es : {familiar1.nombre}, de apellido: {familiar1.apellido} nacido el dia: {familiar1.bd} con una edad de: {familiar1.edad}"
    return HttpResponse(documento)

def familiar2(self):

    familiar2=Familia(nombre="Mauro",apellido="Riso",bd="1998-03-11",edad=24 )
    familiar2.save()
    documento =f"El nombre del familiar es : {familiar2.nombre}, de apellido: {familiar2.apellido} nacido el dia: {familiar2.bd} con una edad de: {familiar2.edad}"
    return HttpResponse(documento)
def familiar3(self): 

    familiar3=Familia(nombre="Ailin",apellido="Sosa",bd="2000-06-11",edad=22 )
    familiar3.save()
    documento =f"El nombre del familiar es : {familiar3.nombre}, de apellido: {familiar3.apellido} nacido el dia: {familiar3.bd} con una edad de: {familiar3.edad}"
    
    return HttpResponse(documento)