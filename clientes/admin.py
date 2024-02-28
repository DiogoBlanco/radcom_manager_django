from django.contrib import admin
from .models import Customer, Contract, File
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    admin.site.register(Customer)


class ContractAdmin(admin.ModelAdmin):
    admin.site.register(Contract)


class FileAdmin(admin.ModelAdmin):
    admin.site.register(File)
