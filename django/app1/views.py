from django.shortcuts import render

# Create your views here.

def helloworld(request):
    versao = "Versão 0.0 de 19/08/2022 10:12"

    return render(request, 'about.html',
        {'data' : versao}
    )