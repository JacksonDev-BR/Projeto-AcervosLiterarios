from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Aqui esta a minha parte por enquanto professora, usei os slides de referencia</h1>")
# Create your views here.
