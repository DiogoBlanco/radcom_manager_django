from django.contrib import admin
from .models import Customer, Contract
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    admin.site.register(Customer)


class ContractAdmin(admin.ModelAdmin):
    admin.site.register(Contract)
