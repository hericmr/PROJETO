from django.db import models
from django.urls import reverse


# Create your models here.
class Poema(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    exceto = models.TextField(null=True, blank=True)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('poema_detalhe', kwargs={'pk': self.pk})

    def __str__(self):
        return self.titulo


