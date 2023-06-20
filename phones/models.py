from django.db import models
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify


class Phone(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.URLField(max_length=200)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    # TODO: Добавьте требуемые поля

