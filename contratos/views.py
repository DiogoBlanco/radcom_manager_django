from django.shortcuts import render, redirect, get_object_or_404
from clientes.models import Contract
from .forms import ContractForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def contratos(request):
    contracts = Contract.objects.all().order_by('customer')

    total_value = sum(contract.value for contract in contracts)

    paginator = Paginator(contracts, 10)
    page = request.GET.get('page')
    try:
        contracts_list = paginator.page(page)
    except PageNotAnInteger:
        contracts_list = paginator.page(1)
    except EmptyPage:
        contracts_list = paginator.page(paginator.num_pages)
    context = {
        'contracts_list': contracts_list,
        'total_value': total_value
    }
    return render(request, 'contratos/index.html', context)


def add_contract(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contratos')
    else:
        form = ContractForm()
    return render(request, 'contratos/add_contrato.html', {'form': form})


def edit_contract(request, contract_id):
    contract = get_object_or_404(Contract, id=contract_id)
    if request.method == 'POST':
        form = ContractForm(request.POST, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('/contratos')
    else:
        form = ContractForm(instance=contract)
    return render(request, 'contratos/edit_contrato.html', {'form': form})


def delete_contract(request, contract_id):
    contract = get_object_or_404(Contract, id=contract_id)
    if request.method == 'POST':
        contract.delete()
        return redirect('/contratos')
    return redirect('/contratos')
