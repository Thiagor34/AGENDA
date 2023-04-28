from django.shortcuts import render, HttpResponse
from . models import Contatos

# Create your views here.
def index(request):
    contatos = Contatos.objects.all()    
    return render(request, 'pages/index.html', {'contatos':contatos})


def search(request): 
    q = request.GET.get('search')   
    contatos = Contatos.objects.filter(nome__icontains=q)    
    return render(request, 'pages/index.html', {'contatos':contatos})
