from django.shortcuts import render, redirect, get_object_or_404
from clientes.models import Contract
from .forms import ContractForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.db.models import Sum


def contratos(request):
    search_query = request.GET.get('search', '')

    all_contracts = Contract.objects.all()

    if search_query:
        contracts = Contract.objects.filter(
            Q(name__icontains=search_query)).order_by('customer')
    else:
        contracts = all_contracts.order_by('customer')

    total_value = all_contracts.aggregate(Sum('value'))['value__sum'] or 0

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
        'total_value': total_value,
        'search_query': search_query
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
