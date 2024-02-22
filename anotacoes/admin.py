from django.contrib import admin
from .models import Annotation

# Register your models here.


class AnnotationAdmin(admin.ModelAdmin):
    admin.site.register(Annotation)
