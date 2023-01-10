from rest_framework import viewsets
from to_do_list.models import Tarefa
from to_do_list.serializer import TarefaSerializer
from rest_framework.permissions import IsAuthenticated


class TarefaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TarefaSerializer

    def get_queryset(self):
        queryset = Tarefa.objects.all()
        username = self.request.user
        if username is not None:
            queryset = queryset.filter(autor=username)
        return queryset
