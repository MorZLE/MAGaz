from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Goods(models.Model):
    """Товары"""
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
    """Категории"""
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('cat', kwargs={'cat': self.pk})


class BasketQuerySet(models.QuerySet):
    """Подсчёт суммы в корзине """
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_qu(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    """Корзина"""
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, verbose_name='Пользователь')
    product = models.ForeignKey(to=Goods, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Кол-во')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')
    objects = BasketQuerySet.as_manager()

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = 'Корзина'
        ordering = ['user']

    def __str__(self):
        return f'Корзина для {self.user.name} | товар: {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity


class RecipientData(models.Model):
    """Данные получателя"""
    recipient = models.CharField(max_length=100, verbose_name='ФИО получателя')
    address = models.TextField(max_length=200, verbose_name='Адрес')
    number = models.CharField(max_length=15, verbose_name='Номер телефона')
    email = models.CharField(max_length=50, verbose_name='Почта')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.recipient

    class Meta:
        verbose_name = "Данные доставки"
        verbose_name_plural = 'Данные доставки'
        ordering = ['recipient']


class StatusOrder(models.Model):
    status = models.CharField(max_length=100, db_index=True, default='1', verbose_name='Статус заказа',)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = 'Статус'
        ordering = ['status']


class Order(models.Model):
    RecipientData = models.ForeignKey(RecipientData, related_name='RecipientData', on_delete=models.CASCADE,
                                      verbose_name='Данные получателя')
    paid = models.BooleanField(default=False, verbose_name='Оплата')
    status = models.ForeignKey(StatusOrder, on_delete=models.CASCADE, verbose_name='Статус заказа', default=1)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = 'Заказ'
        ordering = ['RecipientData']


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='Данные заказа')
    product = models.ForeignKey(Goods, related_name='order_items', on_delete=models.CASCADE, verbose_name='Товар')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    class Meta:
        verbose_name = "Товары заказа"
        verbose_name_plural = 'Товары заказа'
        ordering = ['order']

    def __str__(self):
        return '{}'.format(self.pk)
