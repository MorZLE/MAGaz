from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Goods(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    Quantity = models.IntegerField(null=True, verbose_name='Кол-во')
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    price = models.FloatField(null=True, verbose_name='Цена')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('good', kwargs={'good': self.pk})

    class Meta:
        verbose_name = "Товары"
        verbose_name_plural = 'Товары'
        ordering = ['title', 'category']


class Categories(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('cat', kwargs={'cat': self.pk})


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Goods, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.name} | товар: {self.product.name}'
