from rest_framework import viewsets
from to_do_list.models import Tarefa
from to_do_list.serializer import TarefaSerializer
from rest_framework.permissions import IsAuthenticated


class TarefaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
