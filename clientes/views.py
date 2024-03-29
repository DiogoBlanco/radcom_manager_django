from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Customer
from .forms import CustomerForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


@login_required
def customers(request):
    search_query = request.GET.get('search', '')
    customers = Customer.objects.filter(
        Q(name__icontains=search_query)).order_by('name')
    paginator = Paginator(customers, 10)
    page = request.GET.get('page')
    try:
        customers_list = paginator.page(page)
    except PageNotAnInteger:
        customers_list = paginator.page(1)
    except EmptyPage:
        customers_list = paginator.page(paginator.num_pages)
    context = {
        'customers_list': customers_list,
        'search_query': search_query
    }
    return render(request, 'clientes/index.html', context)


@login_required
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/app')
    else:
        form = CustomerForm()
    return render(request, 'clientes/add_cliente.html', {'form': form})


@login_required
def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/app')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'clientes/edit_cliente.html', {'form': form})


@login_required
def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    return render(request, 'clientes/detalhes_cliente.html', {'customer': customer})


@login_required
def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        customer.delete()
        return redirect('/app')
    return redirect('/app')
