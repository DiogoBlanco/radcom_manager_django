from django.shortcuts import render, redirect, get_object_or_404
from .models import Service
from .forms import ServiceForm

# Create your views here.


def services(request):
    services = Service.objects.all()
    context = {
        'services': services,
    }
    return render(request, 'atendimentos/index.html', context)


def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/atendimentos')
    else:
        form = ServiceForm()
    return render(request, 'atendimentos/add_atendimento.html', {'form': form})


def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('/atendimentos')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'atendimentos/edit_atendimento.html', {'form': form})


def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        service.delete()
        return redirect('/atendimentos')
    return redirect('/atendimentos')
