from django.db import models


class Annotation(models.Model):
    title = models.CharField(max_length=99)
    date = models.DateField()
    reminder = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Anotação'
        verbose_name_plural = 'Anotações'
