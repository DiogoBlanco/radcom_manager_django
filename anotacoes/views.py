from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Annotation
from .forms import AnnotationForm


def annotations(request):
    annotations = Annotation.objects.all().order_by('date')
    context = {
        'annotations': annotations
    }
    return render(request, 'anotacoes/index.html', context)


def add_annotation(request):
    if request.method == 'POST':
        form = AnnotationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Anotação criada com sucesso!')
            return redirect('/anotacoes')
    else:
        form = AnnotationForm()
    return render(request, 'anotacoes/add_anotacao.html',
                  {'form': form})


def edit_annotation(request, annotation_id):
    annotation = get_object_or_404(Annotation, id=annotation_id)
    if request.method == 'POST':
        form = AnnotationForm(request.POST, request.FILES, instance=annotation)
        if form.is_valid():
            form.save()
            return redirect('/anotacoes')
    else:
        form = AnnotationForm(instance=annotation)
    return render(request, 'anotacoes/edit_anotacao.html', {'form': form})


def delete_annotation(request, annotation_id):
    annotation = get_object_or_404(Annotation, id=annotation_id)
    if request.method == 'POST':
        annotation.delete()
        return redirect('/anotacoes')
    return redirect('/anotacoes')
