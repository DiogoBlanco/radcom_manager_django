from django.shortcuts import render
from .models import Customer
# Create your views here.


def customers(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers,
    }
    return render(request, 'clientes/index.html', context)
