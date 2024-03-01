from django.db import models
from clientes.models import Customer


class Files(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Data de Criação')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Última Atualização')
    customer = models.ForeignKey(
        Customer, on_delete=models.DO_NOTHING, verbose_name='Cliente')
    title = models.CharField(max_length=99, verbose_name='Título')
    backup_pabx = models.FileField(
        blank=True, verbose_name='Backup PABX', upload_to='files/pabx')
    backup_rb = models.FileField(
        blank=True, verbose_name='Backup RB', upload_to='files/rb')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Arquivo'
        verbose_name_plural = 'Arquivos'
