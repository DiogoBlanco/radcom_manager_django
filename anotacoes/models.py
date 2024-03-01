from django.db import models


class Annotation(models.Model):
    title = models.CharField(max_length=99, verbose_name='Título')
    reminder = models.TextField(verbose_name='Lembrete')
    image = models.ImageField(verbose_name='Imagem', blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Data de Criação')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Última Atualização')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Anotação'
        verbose_name_plural = 'Anotações'
