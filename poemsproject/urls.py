from django.contrib import admin
from django.urls import path
from poems import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('sobre/', views.sobre, name='sobre'),
    path('<int:pk>/', views.poema_detalhe, name='poema_detalhe'),
    path('noticias/', views.noticias, name='noticias'),  # Defina o padrão de URL para a visualização de notícias
]
