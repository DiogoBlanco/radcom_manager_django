# Generated by Django 5.0.2 on 2024-02-29 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anotacoes', '0003_alter_annotation_date_alter_annotation_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation',
            name='image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Imagem'),
        ),
    ]
