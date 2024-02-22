from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=99)
    address = models.CharField(max_length=99)
    contact = models.CharField(max_length=99)
    equipment = models.TextField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Contract(models.Model):
    contract_type_choices = (('Internet', 'Internet'),
                             ('Interfone', 'Interfone'),
                             ('Internet/Interfone', 'Internet/Interfone'))

    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    contract_type = models.CharField(
        choices=contract_type_choices, max_length=18)
    value = models.DecimalField(decimal_places=2, max_digits=6, default=0.00)

    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'

    def __str__(self):
        return f'{self.customer}'

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
