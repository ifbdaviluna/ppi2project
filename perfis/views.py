from django.shortcuts import render
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html')

def exibir(request, perfil_id):

    perfil = Perfil()

    if perfil_id == 1:
        perfil = Perfil('Davi Luna', 'davi.luna@ifb.edu.br', '111111', 'IFB')
    if perfil_id == 2:
        perfil = Perfil('Marcos Rian', 'marcos.rian@ifb.edu.br', '40028922', 'IESB')

    return render(request, 'perfil.html', {'perfil' : perfil})
# Create your views here.
