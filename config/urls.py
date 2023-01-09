from django.contrib import admin
from django.urls import path, include
from to_do_list.views import TarefaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tarefas', TarefaViewSet, basename='tarefas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('users/', include('users.urls')),
]
