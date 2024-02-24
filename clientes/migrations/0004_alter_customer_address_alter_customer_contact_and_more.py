# Generated by Django 5.0.2 on 2024-02-24 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_alter_customer_equipment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=99, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='contact',
            field=models.CharField(max_length=99, verbose_name='Contato'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='equipment',
            field=models.TextField(null=True, verbose_name='Equipamento'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=99, verbose_name='Nome'),
        ),
    ]
