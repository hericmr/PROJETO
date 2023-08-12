from django.contrib import admin
from django.urls import path
from poems import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('sobre/', views.sobre, name='sobre'),
    path('<int:pk>/', views.poema_detalhe, name='poema_detalhe'),
    path('noticias/', views.noticias, name='noticias'),  # Defina o padrão de URL para a visualização de notícias
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
