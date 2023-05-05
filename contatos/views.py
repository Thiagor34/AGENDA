from django.shortcuts import render, redirect
from . models import Contatos

# Create your views here.
def index(request):
    contatos = Contatos.objects.all()    
    return render(request, 'pages/index.html', {'contatos':contatos})


def search(request): 
    q = request.GET.get('search')   
    contatos = Contatos.objects.filter(nome__icontains=q)    
    return render(request, 'pages/index.html', {'contatos':contatos})

def detalhes(request, id):
    contato = Contatos.objects.get(id=id)
    return render(request, 'pages/detalhes.html', {'contato':contato})

def deletar(request, id):
    contato = Contatos.objects.get(id=id)
    contato.delete()
    return redirect('home')  

def adicionar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        altura = request.POST.get('altura')
        descricao = request.POST.get('descricao')
        data_nascimento = request.POST.get('data_nascimento')
        imagem = request.FILES.get('imagem')
        
        novo_contato = Contatos(nome=nome, cpf=cpf, email=email, telefone=telefone, altura=altura, descricao=descricao, data_nascimento=data_nascimento,imagem=imagem, ativo=True)
        novo_contato.save()
        redirect('home')
    
    else:
        return render(request, 'pages/adicionar.html')