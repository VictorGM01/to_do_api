# To Do List API

## Descrição do Projeto 📋
Esta é uma API desenvolvida com o Django Rest Framework, a qual funciona como uma lista de tarefas (to do list).
Nesse viés, tal API possibilita a criação de tarefas com os seguintes campos: título, descrição, data de
conclusão e status de conclusão. Além de criar, também é possível listar, atualizar e deletar tarefas.

<div align="center">
    <img alt="Badge com a versão utilizada do Python" src="https://img.shields.io/static/v1?label=PYTHON&message=3.9.9&color=blue&style=for-the-badge&logo=Python"/>
    <img alt="Badge com a versão utilizada do Django" src="https://img.shields.io/static/v1?label=DJANGO&message=4.0.1&color=brightgreen&style=for-the-badge&logo=DJANGO&logoColor=green"/>
    <img alt="Badge com a versão utilizada do Django" src="https://img.shields.io/static/v1?label=D.R.F&message=3.14.0&color=red&style=for-the-badge&logo=DJANGO&logoColor=red"/>
</div>

## Estrutura de Pastas 🗂️
* Raíz

    ├── config <br>
    ├── to_do_list <br>
        &emsp;&emsp; └── migrations <br>
    ├ manage.py <br>
    ├ README.md <br>

Na pasta raiz, há dois arquivos principais:

* README.md: guia sobre os aspectos do projeto
* manage.py: *script* que auxilia na gestão da API

Ademais, há duas pastas, as quais estão organizadas do seguinte modo:

* config: pasta do *django project*, responsável por organizar todos os arquivos de configuração do projeto;
* to_do_list: pasta do *django app*, responsável por organizar os arquivos relacionados ao aplicativo das tarefas.

## Demonstração da Aplicação 💻
> Dados para a inclusão de uma tarefa - post

<img src="https://user-images.githubusercontent.com/86068797/209858395-8e87eb76-bf26-48c2-a279-6f0c7a55fe6a.png" alt="imagem com o conteúdo necessário para a inclusão de uma tarefa" title="Conteúdo necessário para a inclusão de uma tarefa">

> Listagem das tarefas - get /tarefas/

<img src="https://user-images.githubusercontent.com/86068797/209858766-75770773-f536-4f9d-8852-956e52d6ef84.png" alt="imagem com o conteúdo listado a partir do método get" title="Listagem das tarefas via GET">