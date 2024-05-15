from django.shortcuts import render


# Função responsavel pela pagina principal da aplicação
# Receb o request e responde
def index(request):
    return render(request, 'galeria/index.html')
    
def imagem(request):
    return render(request, 'galeria/imagem.html')
    


