from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, File
from .forms import CustomerForm, FileForm

# Create your views here.


def customers(request):
    customers = Customer.objects.all().order_by('name').values()
    context = {
        'customers': customers,
    }
    return render(request, 'clientes/index.html', context)


def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/clientes')
    else:
        form = CustomerForm()
    return render(request, 'clientes/add_cliente.html', {'form': form})


def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/clientes')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'clientes/edit_cliente.html', {'form': form})


def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    return render(request, 'clientes/detalhes_cliente.html', {'customer': customer})


def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        customer.delete()
        return redirect('/clientes')
    return redirect('/clientes')


def file_upload(request, customer_id):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save()
            customer = Customer.objects.get(pk=customer_id)
            customer.files.add(file)
            return redirect('/clientes')
    else:
        form = FileForm()
    return render(request, 'clientes/enviar_arquivo.html', {'form': form})
