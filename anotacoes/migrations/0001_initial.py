# Generated by Django 5.0.2 on 2024-02-29 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=99, verbose_name='Título')),
                ('date', models.DateField(verbose_name='Data')),
                ('reminder', models.TextField(verbose_name='Lembrete')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Imagem')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Última Atualização')),
            ],
            options={
                'verbose_name': 'Anotação',
                'verbose_name_plural': 'Anotações',
            },
        ),
    ]
