# Generated by Django 5.0.2 on 2024-02-29 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anotacoes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annotation',
            name='date',
        ),
    ]
