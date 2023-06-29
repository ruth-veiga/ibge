from django.shortcuts import render, redirect
from .models import Pessoa
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request,'pessoas.html',{'pessoas': pessoas} )

def cadastrar_pessoa(request):
    nome_pessoa = request.POST.get('nome_pessoa')
    cor_pessoa = request.POST.get('cor')
    idade_pessoa = request.POST.get('idade')
    genero_pessoa = request.POST.get('genero')
    salario_pessoa = request.POST.get('salario')

    Pessoa.objects.create(nome=nome_pessoa, cor= cor_pessoa, idade= idade_pessoa, genero= genero_pessoa, salario= salario_pessoa)
     
    return redirect(lista_pessoas)
# Create your views here.
