from django.shortcuts import render
from .models import Annotation

# Create your views here.


def annotations(request):
    annotations = Annotation.objects.all()
    context = {
        'annotations': annotations
    }
    return render(request, 'anotacoes/index.html', context)
