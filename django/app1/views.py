from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import PessoasForm
from django.http import HttpResponseRedirect
from .models import Pessoas
from django.contrib import messages
# Create your views here.

@login_required
def index(request):

    data = "Versão 0.1"

    return render(request, 'index.html',
                    {'dados': data}
                    )

# @login_required
# def db1(request):

#     data = "Versao 0.01 - Dashboard 1 (um) "

#     return render(request, 'dashboard1.html',
#                   {'dados': data}
#                   )


# @login_required
# def db2(request):

#     data = "Versao 0.01 - Dashboard 2 (dois)"

#     return render(request, 'dashboard2.html',
#                   {'dados': data}
#                   )


# @login_required
# def pessoasview(request):

#     if request.method == 'POST':
#         form = PessoasForm(request.POST)
#         if form.is_valid():
#             nova_pessoa = form.save(commit=False)
#             nova_pessoa.pessoa_nome = form.cleaned_data['pessoa_nome']
#             nova_pessoa.pessoa_idade = form.cleaned_data['pessoa_idade']
#             nova_pessoa.save()
#             return HttpResponseRedirect('/pessoas/')
#     else:
#         form = PessoasForm()
#     pessoas = Pessoas.objects.all()
    
#     return render(request, 'pessoasview.html',
#                   {
#                       'form': form,
#                       'pessoas' : pessoas
#                   }

#                   )


# @login_required
# def thanks(request):
#     mensagem = "Obrigado!"
#     return render(request, 'thanks.html', {'mensagem': mensagem}
#                   )

@login_required
def pessoas_list(request):
    search = request.GET.get('search')
    if search:
        pessoas = Pessoas.objects.filter(pessoa_nome__icontains=search)
    else:
        pessoas = Pessoas.objects.all()

    return render(request, 'pessoas_list.html',
                  {'pessoas': pessoas})

@login_required
def pessoa_add(request, id=0):
    if request.method == 'POST':
        form = PessoasForm(request.POST)
        if form.is_valid():
            nova_pessoa = form.save(commit=False)
            nova_pessoa.pessoa_nome = form.cleaned_data['pessoa_nome']
            nova_pessoa.pessoa_idade = form.cleaned_data['pessoa_idade']
            nova_pessoa.save()
            return HttpResponseRedirect('/pessoas_list')
    else:
        form = PessoasForm()
        
    pessoas = Pessoas.objects.all()

    return render(request, 'pessoa_add.html',
                    {
                        'form': form,
                        'pessoas': pessoas
                    }
                    )   

@login_required
def pessoa_edit(request, id):
    pessoa = get_object_or_404(Pessoas, pk=id)
    form = PessoasForm(instance=pessoa)
    if ( request.method == 'POST'):
        form = PessoasForm(request.POST, instance=pessoa)
        if (form.is_valid()):
            pessoa.save()
            return redirect('/pessoas_list')
        else:
            return render(request, 'pessoa_edit.html', {'form': form, 'pessoa': pessoa})
    else:
        return render(request, 'pessoa_edit.html', {'form': form, 'pessoa': pessoa})

@login_required
def pessoa_delete(request, id):
    pessoa = get_object_or_404(Pessoas, pk=id)
    pessoa.delete()
    messages.info(request, 'Pessoa apagado do banco de dados')
    return redirect('/pessoas_list')



