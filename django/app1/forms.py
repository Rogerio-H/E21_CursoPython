from django import forms
from .models import Pessoas


class PessoasForm(forms.Form):
    pessoas_nome = forms.CharField(label = 'Nome ', max_length=100)
    pessoas_idade = forms.IntegerField(label= 'Idade ')

    class Meta:
        model = Pessoas
        fields = ('pessoa_nome', 'pessoa_idade')
    