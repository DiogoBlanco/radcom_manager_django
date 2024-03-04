from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Annotation
from .forms import AnnotationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


@login_required
def annotations(request):
    search_query = request.GET.get('search', '')
    annotations = Annotation.objects.filter(
        Q(title__icontains=search_query)).order_by('title')
    paginator = Paginator(annotations, 10)
    page = request.GET.get('page')
    try:
        annotations_list = paginator.page(page)
    except PageNotAnInteger:
        annotations_list = paginator.page(1)
    except EmptyPage:
        annotations_list = paginator.page(paginator.num_pages)
    context = {
        'annotations_list': annotations_list,
        'search_query': search_query
    }
    return render(request, 'anotacoes/index.html', context)


@login_required
def add_annotation(request):
    if request.method == 'POST':
        form = AnnotationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/app/anotacoes')
    else:
        form = AnnotationForm()
    return render(request, 'anotacoes/add_anotacao.html',
                  {'form': form})


@login_required
def edit_annotation(request, annotation_id):
    annotation = get_object_or_404(Annotation, id=annotation_id)
    if request.method == 'POST':
        form = AnnotationForm(request.POST, request.FILES, instance=annotation)
        if form.is_valid():
            form.save()
            return redirect('/app/anotacoes')
    else:
        form = AnnotationForm(instance=annotation)
    return render(request, 'anotacoes/edit_anotacao.html', {'form': form})


@login_required
def delete_annotation(request, annotation_id):
    annotation = get_object_or_404(Annotation, id=annotation_id)
    if request.method == 'POST':
        annotation.delete()
        return redirect('/app/anotacoes')
    return redirect('/app/anotacoes')
