from django.db import models

# Create your models here.


class File(models.Model):
    file = models.FileField(
        upload_to='files/', blank=True, verbose_name='Arquivo')
    description = models.CharField(
        max_length=255, blank=True, verbose_name='Descrição')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Arquivo'
        verbose_name_plural = 'Arquivos'


class Customer(models.Model):
    name = models.CharField(max_length=99, verbose_name='Nome')
    address = models.CharField(max_length=99, verbose_name='Endereço')
    contact = models.CharField(max_length=99, verbose_name='Contato')
    equipment = models.TextField(
        blank=True, null=True, verbose_name='Equipamento')
    files = models.ManyToManyField(File, blank=True, verbose_name='Arquivos')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Contract(models.Model):
    contract_type_choices = (('Internet', 'Internet'),
                             ('Interfone', 'Interfone'),
                             ('Internet/Interfone', 'Internet/Interfone'))

    customer = models.ForeignKey(
        Customer, on_delete=models.DO_NOTHING, verbose_name='Cliente')
    contract_type = models.CharField(
        choices=contract_type_choices, max_length=18, verbose_name='Tipo de Contrato')
    value = models.DecimalField(
        decimal_places=2, max_digits=6, default=0.00, verbose_name='Valor')

    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'

    def __str__(self):
        return f'{self.customer}'

    def name(self):
        return self.customer.name

    def set_contract_value(self):
        if self.contract_type == 'Internet':
            self.value = 100.00
        elif self.contract_type == 'Interfone':
            self.value = 56.00
        elif self.contract_type == 'Internet/Interfone':
            self.value = 156.00
        else:
            self.value = 0

    def save(self, *args, **kwargs):
        self.set_contract_value()  # Call set_contract_value before saving
        super(Contract, self).save(*args, **kwargs)
