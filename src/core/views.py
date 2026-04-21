from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "core/index.html")


def saludar(request):
    return HttpResponse("Hola!!!")


def saludar_con_etiqueta(request):
    return HttpResponse("<h1>Hola!!!</h1><p>cómo estás</p>")
