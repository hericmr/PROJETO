from django.contrib import admin
from django.urls import path
from poems import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
]
