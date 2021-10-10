from django.urls import path
from .views import *


urlpatterns = [
    path('', mostrarTemplate, name='mostrar_view'),
    path('mudarstatus/<int:id>', mudarStatus, name="mudar-status"),
    path('novoElemento/', criarElemento, name='novo_elemento'),
    path('deletar/<int:id>', deletarElemento, name="deletar"),
    path('editarCrud/<int:id>', editarElemento, name="editar_crud"),
    path('pegarValores/<int:id>', pegarValores, name='pegarValores'),
    
]
