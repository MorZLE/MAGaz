from django.db import models
from django.urls import reverse


class Goods(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    Quantity = models.IntegerField(null=True)
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True)
    price = models.FloatField(null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('good', kwargs={'good': self.pk})


class Categories(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cat', kwargs={'cat': self.pk})
