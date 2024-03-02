from django.shortcuts import render, redirect, get_object_or_404
from .models import Files
from .forms import FilesForm


def file(request):
    files = Files.objects.all().order_by('customer')
    return render(request, 'arquivos/index.html', {'files': files})


def add_file(request):
    if request.method == 'POST':
        form = FilesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/arquivos')
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
            return redirect('/arquivos')
    else:
        form = FilesForm(instance=file)
    return render(request, 'arquivos/edit_arquivos.html', {'form': form, 'file': file})


def delete_file(request, file_id):
    file = get_object_or_404(Files, id=file_id)
    if request.method == 'POST':
        file.delete()
        return redirect('/arquivos')
    return redirect('/arquivos')
