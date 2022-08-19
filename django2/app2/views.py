from django.shortcuts import render

# Create your views here.

def helloworld(request):
    versao = "Versão 0.1 de 19/08/2022 11:22"

    return render(request, 'about.html',
        {'data' : versao}
    )
