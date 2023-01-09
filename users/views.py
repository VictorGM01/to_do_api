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
