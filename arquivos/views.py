from django.shortcuts import render, redirect
from .models import Files
from .forms import FilesForm


def index(request):
    files = Files.objects.all().order_by('customer')
    context = {
        'files': files
    }
    return render(request, 'arquivos/index.html', context)


def add_files(request):
    if request.method == 'POST':
        form = FilesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/arquivos')
    else:
        form = FilesForm()
    return render(request, 'arquivos/add_arquivos.html',
                  {'form': form})
