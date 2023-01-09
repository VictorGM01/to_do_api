from django.contrib.auth.models import User
from django.contrib import auth
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def cadastro(request):
    """Cadastra um novo usuário no sistema"""
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']

        if User.objects.filter(email=email).exists():
            return Response({'status': 'e-mail já cadastrado'}, status=status.HTTP_404_NOT_FOUND)

        elif User.objects.filter(username=nome).exists():
            return Response({'status': 'username já utilizado'}, status=status.HTTP_404_NOT_FOUND)

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()

        return Response({'status': 'criado'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login(request):
    """Realiza o login do usuário no sistema"""
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()

            user = auth.authenticate(request, username=nome, password=senha)

            if user is not None:
                auth.login(request, user)
                return Response({'status': 'autenticado'}, status=status.HTTP_200_OK)

            else:
                return Response({'status': 'senha incorreta'}, status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response({'status': 'usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
