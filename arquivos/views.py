from django.shortcuts import render


def index(request):
    return render(request, 'arquivos/index.html')
