from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class Tarefa(object):
    """docstring for ."""
    def __init__(self, titulo, data):
        self.titulo = titulo
        self.data = data

    def __str__(self):
        return self.titulo

def home(request):
    return HttpResponse("Olá")

def sobre(request):
    return HttpResponse("Clara Macêdo")

def tarefa(request, ano, mes, dia, minuto):
    return HttpResponse("Tarefa: "+str(dia)+"-"+str(mes)+"-"+str(ano)+":"+str(minuto))
