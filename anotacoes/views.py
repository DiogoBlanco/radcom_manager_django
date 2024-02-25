from django.shortcuts import render, get_object_or_404, redirect
from .models import Annotation
from .forms import AnnotationForm

# Create your views here.


def annotations(request):
    annotations = Annotation.objects.all()
    context = {
        'annotations': annotations
    }
    return render(request, 'anotacoes/index.html', context)


def add_annotation(request):
    if request.method == 'POST':
        form = AnnotationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/anotacoes')
    else:
        form = AnnotationForm()
    return render(request, 'anotacoes/add_anotacao.html', {'form': form})


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
