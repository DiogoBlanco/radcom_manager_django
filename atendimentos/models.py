from django.db import models
from clientes.models import Customer

# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=99, verbose_name='Nome', default='')
    customer = models.ForeignKey(
        Customer, on_delete=models.DO_NOTHING, verbose_name='Cliente')
    date = models.DateField(max_length=10, verbose_name='Data')
    problem = models.TextField(verbose_name='Problema')
    solution = models.TextField(verbose_name='Solução')
    value = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Valor')
    image = models.ImageField(verbose_name='Imagem', blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Data de Criação')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Última Atualização')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Atendimento'
        verbose_name_plural = 'Atendimentos'
