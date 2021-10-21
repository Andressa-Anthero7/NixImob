from django.shortcuts import render
from .forms import PropostaForm
from .models import Imagens, Perfil

# Create your views here.

def index(request):
    if request.method == 'POST':
        formulario = PropostaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return render(request, 'nix-imob/index.html')
    formulario = PropostaForm()
    img = Imagens.objects.all()
    dados = Perfil.objects.all()
    return render(request, 'nix-imob/index.html',{'formulario': formulario,'img':img,'dados': dados})