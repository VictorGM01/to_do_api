from django.db import models
from django.utils import timezone


class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    data = models.DateField(default=timezone.now(), blank=True, null=True)
    concluida = models.BooleanField(default=False)
    descricao = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.titulo
