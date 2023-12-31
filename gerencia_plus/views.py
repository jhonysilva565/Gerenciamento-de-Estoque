from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.http import Http404
from django.http import HttpResponseRedirect
from .models import Gerenciamento, Contato
from django.contrib.auth import authenticate, login as auth_login
from .models import Login
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    return render(request, 'gerenciamento/index.html')

def cadastro(request):
    return render(request, 'cadastro.html')
        
def inicial(request):
    return render(request, 'inicial.html')

from django.shortcuts import render, redirect
from .models import Gerenciamento

@login_required  # Adicione o decorador para garantir que apenas usuários autenticados possam acessar esta view
def salvo(request):
    if request.method == 'POST':
        gere = Gerenciamento()
        gere.user = request.user  # Associe o usuário autenticado ao produto
        gere.nome_produto = request.POST.get('nome-produto')
        gere.quantidade = request.POST.get('quantidade')
        gere.descricao = request.POST.get('descricao')
        gere.peso = request.POST.get('peso-estoque')
        gere.preco = request.POST.get('preco')
        gere.fornecedor = request.POST.get('fornecedor')
        gere.categoria = request.POST.get('categoria')
        gere.data_entrada = request.POST.get('data-entrada')
        gere.save()

        return redirect('salvo')  # substitua por nome da URL que mostra a lista de produtos

    else:
        cadastro_estoque = {
            'cadastro_estoque': Gerenciamento.objects.filter(user=request.user)  # Filtra os produtos pelo usuário autenticado
        }

        return render(request, 'estoque.html', cadastro_estoque)


def avaliar(request):
    return render(request, 'avaliar.html')

def sucesso(request):
    return render(request, 'sucesso.html')

def contato(request):
    return render(request, 'contato.html')

def emailsucesso(request):
    return render(request, 'emailsucesso.html')

def turorial(request):
    return render(request, 'tutorial.html')

def sucesso(request):
    if request.method == 'POST':
        rating = request.POST['rating']
        feedback = request.POST['feedback']
        review = avaliar(rating=rating, feedback=feedback)
        review.save()
        return HttpResponseRedirect('/sucesso/')

    return render(request, 'sucesso.html')

class EstoqueDeleteView(APIView):
    def get_object(self, pk):
        try:
            return Gerenciamento.objects.get(pk=pk)
        except Gerenciamento.DoesNotExist:
            raise Http404
    
    def delete(self, request, pk):
        estoque = self.get_object(pk)
        estoque.delete()
        return Response(status=204)
    
def enviar_formulario(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        mensagem = request.POST['mensagem']

        # Crie um novo objeto Contato e salve-o no banco de dados
        contato = Contato(nome=nome, email=email, mensagem=mensagem)
        contato.save()

        return redirect('emailsucesso')  # Substitua 'sucesso' pela URL da página de sucesso desejada

    return render(request, 'contato.html')
# Substitua 'formulario.html' pelo nome do seu template de formulário


def register(request):
    user_exists_error = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            if User.objects.filter(username=username).exists():
                user_exists_error = True
            elif len([c for c in username if c.isdigit()]) < 3 or len([c for c in password if c.isdigit()]) < 3:
                messages.error(request, 'O nome de usuário e a senha devem conter pelo menos 3 números.')
            else:
                user = User.objects.create_user(username=username, password=password)
                
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    return redirect('home')
    
    return render(request, 'register.html', {'user_exists_error': user_exists_error})



def login_view(request):
    error_message = None
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth_login(request, user)
                
                # Crie uma instância do modelo Login e salve as informações no banco de dados
                login_instance = Login(usuario=username, senha=password)
                login_instance.save()

                return redirect('inicial')
            else:
                error_message = 'Usuário ou senha inválidos.'
    
    return render(request, 'login.html', {'error_message': error_message})

def politica_de_privacidade(request):
    return render(request, 'politica_de_privacidade.html')

def termos_de_servico(request):
    return render(request, 'termos_de_servico.html')
