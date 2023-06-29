from django.shortcuts import render
from .models import Pessoa
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request,'pessoas.html',{'pessoas': pessoas} )


# Create your views here.
