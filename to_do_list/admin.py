from django.contrib import admin
from .models import Tarefa


class Tarefas(admin.ModelAdmin):
    list_display = ("id", "titulo", "data", "status")
    list_display_links = ("id", "titulo")
    search_fields = ("titulo", )
    list_editable = ('status', )
    list_filter = ('status',)
    list_per_page = 10


admin.site.register(Tarefa, Tarefas)
