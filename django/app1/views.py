from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PessoasForm
from django.http import HttpResponseRedirect

# Create your views here.

@login_required
def index(request):

    data = "Versão 0.1"

    return render(request, 'index.html',
                    {'dados': data}
                    )

@login_required
def db1(request):

    data = "Versao 0.01 - Dashboard 1 (um) "

    return render(request, 'dashboard1.html',
                  {'dados': data}
                  )


@login_required
def db2(request):

    data = "Versao 0.01 - Dashboard 2 (dois)"

    return render(request, 'dashboard2.html',
                  {'dados': data}
                  )


@login_required
def pessoasview(request):

    if request.method == 'POST':
        form = PessoasForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = PessoasForm()

    return render(request, 'pessoasview.html',
                  {
                      'form': form
                  }

                  )


@login_required
def thanks(request):
    mensagem = "Obrigado!"
    return render(request, 'thanks.html', {'mensagem': mensagem}
                  )







