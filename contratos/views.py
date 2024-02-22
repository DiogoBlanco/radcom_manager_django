from django.shortcuts import render
from clientes.models import Contract


def contratos(request):
    contracts = Contract.objects.all()
    context = {
        'contracts': contracts
    }
    return render(request, 'contratos/index.html', context)
