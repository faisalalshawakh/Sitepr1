from django.http import HttpResponse
from django.shortcuts import render



def index(request):
   HttpResponse("Viva DIAM. Esta e a pagina de entrada da app votacao.")

