# Generated by Django 5.0.2 on 2024-02-20 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_alter_contract_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='equipment',
            field=models.TextField(null=True),
        ),
    ]