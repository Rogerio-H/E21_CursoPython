from socket import fromshare
from django import forms

class PessoasForm(forms.Form):
    pessoas_nome = forms.CharField(label = 'Nome ', max_length=100)
    pessoas_idade = forms.IntegerField(label= 'Idade ')