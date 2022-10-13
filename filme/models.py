from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
# Create your models here.

LISTA_CATEGORIAS = (
    ('ANALISES', 'Analises'),
    ('PROGRAMACAO', 'Programação'),
    ('APRESENTACAO', 'Apresentação'),
    ('OUTROS', 'Outros'),
)

# criar filme
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_de_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo



#criar episodios


#criar usuario