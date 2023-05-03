from django.db import models


class Goods(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    #category = models.ForeignKey('Categories.category', on_delete=True)


class Categories(models.Model):
    category = models.CharField(max_length=100)

