from django.shortcuts import render, redirect, get_object_or_404
from .models import Service
from .forms import ServiceForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def services(request):
    search_query = request.GET.get('search', '')
    services = Service.objects.filter(
        Q(name__icontains=search_query)).order_by('name')
    paginator = Paginator(services, 10)
    page = request.GET.get('page')
    try:
        services_list = paginator.page(page)
    except PageNotAnInteger:
        services_list = paginator.page(1)
    except EmptyPage:
        services_list = paginator.page(paginator.num_pages)

    context = {
        'services_list': services_list,
        'search_query': search_query
    }
    return render(request, 'atendimentos/index.html', context)


def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/app/atendimentos')
    else:
        form = ServiceForm()
    return render(request, 'atendimentos/add_atendimento.html', {'form': form})


def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect('/app/atendimentos')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'atendimentos/edit_atendimento.html', {'form': form})


def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        service.delete()
        return redirect('/app/atendimentos')
    return redirect('/app/atendimentos')
