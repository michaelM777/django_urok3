from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя категории', max_lenght=255, unique=True)
    desc = models.TextField(verbose_name='описание категории', blank=True)

    