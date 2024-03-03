from django.shortcuts import render, redirect, get_object_or_404
from .models import Files
from .forms import FilesForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def file(request):
    search_query = request.GET.get('search', '')
    files = Files.objects.filter(
        Q(title__icontains=search_query)).order_by('customer')
    paginator = Paginator(files, 10)
    page = request.GET.get('page')
    try:
        files_list = paginator.page(page)
    except PageNotAnInteger:
        files_list = paginator.page(1)
    except EmptyPage:
        files_list = paginator.page(paginator.num_pages)
    context = {
        'files_list': files_list,
        'search_query': search_query
    }
    return render(request, 'arquivos/index.html', context)


def add_file(request):
    if request.method == 'POST':
        form = FilesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/app/arquivos')
    else:
        form = FilesForm()
    return render(request, 'arquivos/add_arquivos.html',
                  {'form': form})


def edit_file(request, file_id):
    file = get_object_or_404(Files, id=file_id)
    if request.method == 'POST':
        form = FilesForm(request.POST, request.FILES, instance=file)
        if form.is_valid():
            form.save()
            return redirect('/app/arquivos')
    else:
        form = FilesForm(instance=file)
    return render(request, 'arquivos/edit_arquivos.html', {'form': form, 'file': file})


def delete_file(request, file_id):
    file = get_object_or_404(Files, id=file_id)
    if request.method == 'POST':
        file.delete()
        return redirect('/app/arquivos')
    return redirect('/app/arquivos')
