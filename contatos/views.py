from django.shortcuts import render, redirect, get_object_or_404
from . models import Contatos
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(redirect_field_name='login')
def index(request):
    contatos = Contatos.objects.filter(usuario_id=request.user.id).order_by('-id')   
    return render(request, 'pages/index.html', {'contatos':contatos})


def search(request): 
    q = request.GET.get('search')   
    contatos = Contatos.objects.filter(nome__icontains=q)    
    return render(request, 'pages/index.html', {'contatos':contatos})

def detalhes(request, id):
    # contato = Contatos.objects.get(id=id)
    contato = get_object_or_404(Contatos, id=id)
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
        
        novo_contato = Contatos(usuario_id=request.user.id,nome=nome, cpf=cpf, email=email, telefone=telefone, altura=altura, descricao=descricao, data_nascimento=data_nascimento,imagem=imagem, ativo=True)
        novo_contato.save()
        return redirect('home')
    
    else:
        return render(request, 'pages/adicionar.html')
    
    
def editar(request, id):
    contato = Contatos.objects.get(id=id)    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        altura = request.POST.get('altura')
        descricao = request.POST.get('descricao')
        data_nascimento = request.POST.get('data_nascimento')
        imagem = request.FILES.get('imagem')
        ativo = request.POST.get('ativo')

        if ativo == None:
            ativo = False
        else:
            ativo = True
        
        contato.nome = nome
        contato.cpf = cpf
        contato.email = email
        contato.telefone = telefone
        contato.data = data_nascimento
        if imagem != None:
            contato.imagem = imagem
        contato.altura = altura
        contato.descricao = descricao
        contato.ativo = ativo

        contato.save()  
              
        return redirect('home')
       
    else:
            
        return render(request, 'pages/editar.html', {'contato':contato})