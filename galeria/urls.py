from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
    path('', index, name='index'), # Rota principal -  name indica como a pagina é referenciada no HTML - Ver linha 31 de templates/galeria/imagem.html
    path('imagem/', imagem, name='imagem') # Rota de imagens da aplicação GAleria
]