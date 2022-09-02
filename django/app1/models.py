from django.db import models

# Create your models here.

class Pessoas(models.Model):
    pessoa_nome = models.CharField(max_length=100, verbose_name="Nome")
    pessoa_idade = models.IntegerField(verbose_name="Idade", default=0)