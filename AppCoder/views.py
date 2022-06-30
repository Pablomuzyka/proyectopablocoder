from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso

# Create your views here.


def curso(self):
    curso=Curso(nombre="django", comision=451551)
    curso.save()
    texto=f"curso creado: {curso.nombre} {curso.comision}"
    return HttpResponse(texto)
