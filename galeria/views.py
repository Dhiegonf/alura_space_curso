from django.shortcuts import render
from django.http import HttpResponse

# responsável por exibir o conteúdo nas telas

def index(request):
    return HttpResponse('<h1>Teste ok</h1>')


