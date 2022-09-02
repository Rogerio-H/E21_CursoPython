from django.db import models
from uuid import uuid4
from datetime import datetime

# Create your models here.

class Turmas(models.Model):
    turma_nome = models.CharField(max_length=40)
    ativo = models.CharField(max_length=1)

class Pessoas(models.Model):
    # pessoa_id = models.BigAutoField(primary_key=True)
    # id = models.UUIDField(primary_key=True,default=uuid4, editable=False)
    pessoa_nome = models.CharField(max_length=100,verbose_name="Nome")
    pessoa_idade = models.IntegerField(verbose_name="Idade",default=0)
    PessoaCreate = models.DateTimeField(verbose_name="TimeStamp",auto_now_add=True,blank=True)
    pessoa_ativo = models.CharField(max_length=1,default='S')
    
    # def __str__(self):
    #     return '%s %s' % (self.pessoa_nome, self.pessoa_idade)

    class Meta:
        ordering = ('pessoa_nome', 'pessoa_idade')

class Alunos(Pessoas):
    AlunoCreate = models.DateTimeField(verbose_name="TimeStamp",auto_now_add=True,blank=True)
    codigo_aluno = models.CharField(max_length=10,null=True)
    Alunos_data  = models.DateField()
    Media_Geral_Inteiro = models.IntegerField()
    TIPO = [
        ('P', 'Particular'),
        ('C', 'Convenio')        
    ]
    tipo = models.CharField(max_length=1,choices=TIPO)
    equipe = models.TextChoices('YoungPower', 'OldiesPower')
    turma = models.ForeignKey(Turmas,on_delete=models.CASCADE)
    aluno_ativo = models.CharField(max_length=1,default='S')

# CASCADE: When the referenced object is deleted, also delete the objects that have references to it (when you remove a blog post for instance, you might want to delete comments as well). SQL equivalent: CASCADE.
# PROTECT: Forbid the deletion of the referenced object. To delete it you will have to delete all objects that reference it manually. SQL equivalent: RESTRICT.
# RESTRICT: (introduced in Django 3.1) Similar behavior as PROTECT that matches SQL's RESTRICT more accurately. (See django documentation example)
# SET_NULL: Set the reference to NULL (requires the field to be nullable). For instance, when you delete a User, you might want to keep the comments he posted on blog posts, but say it was posted by an anonymous (or deleted) user. SQL equivalent: SET NULL.
# SET_DEFAULT: Set the default value. SQL equivalent: SET DEFAULT.
# SET(...): Set a given value. This one is not part of the SQL standard and is entirely handled by Django.
# DO_NOTHING: Probably a very bad idea since this would create integrity issues in your database (referencing an object that actually doesn't exist). SQL equivalent: NO ACTION. (2)