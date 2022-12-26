from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from to_do_list.models import Tarefa
from datetime import datetime


class TestTarefas(APITestCase):

    def test_deve_retornar_status_code_200_no_metodo_get(self):
        resposta = self.client.get("/")
        self.assertEqual(resposta.status_code, status.HTTP_200_OK)
