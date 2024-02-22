from django.contrib import admin
from .models import Service
# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    admin.site.register(Service)
