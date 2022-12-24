from django.db import models
from datetime import datetime


class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    data = models.DateField(default=datetime.now(), blank=True)
    status = models.BooleanField(default=False)
    descricao = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.titulo
