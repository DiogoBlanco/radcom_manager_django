from django.db import models
from clientes.models import Customer

# Create your models here.


class Service(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    date = models.DateField(max_length=10)
    problem = models.TextField()
    solution = models.TextField()
    value = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.customer.name

    class Meta:
        verbose_name = 'Atendimento'
        verbose_name_plural = 'Atendimentos'
