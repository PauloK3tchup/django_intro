from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bem-vindo à BSI4 Store! <br/> <a href='/about'>Sobre</a>")

def about(request):
    return HttpResponse("O fim esta próximo <br/> <a href='/'>Home</a>")