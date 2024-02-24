from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm

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
