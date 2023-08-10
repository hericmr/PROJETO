from django.shortcuts import render
from .models import Poema
from . import views
# Create your views here.
def home(request):
    poems = Poema.objects.all()
    context = {'poems': poems}
    return render(request, 'home.html', {'poems': poems})