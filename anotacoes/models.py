from django.db import models


class Annotation(models.Model):
    title = models.CharField(max_length=99, verbose_name='Título')
    date = models.DateField(verbose_name='Data')
    reminder = models.TextField(verbose_name='Lembrete')
    image = models.ImageField(verbose_name='Imagem')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Anotação'
        verbose_name_plural = 'Anotações'
