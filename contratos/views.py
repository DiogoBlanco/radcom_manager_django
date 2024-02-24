from django.shortcuts import render
from clientes.models import Contract


def contratos(request):
    contracts = Contract.objects.all().order_by('customer')
    context = {
        'contracts': contracts
    }
    return render(request, 'contratos/index.html', context)
