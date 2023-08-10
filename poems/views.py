from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Poema
from . import views
# Create your views here.
def home(request):
    poems = Poema.objects.all()
    context = {'poems': poems}
    return render(request, 'home.html', {'poems': poems})

def sobre(request):
    return render(request, 'sobre.html')

def poema_detalhe(request, pk):
    poema = get_object_or_404(Poema, id=pk)
    context = {'poem': poema}  # Corrigido de 'contexto' para 'context'
    return render(request, 'poema_detalhe.html', context)
    
from django.shortcuts import render

def noticias(request):
    # Your view logic for noticias goes here
    # For example, you can retrieve news articles from a database or an external API
    context = {
        'articles': [...]  # Replace with your actual list of articles
    }
    return render(request, 'noticias.html', context)
