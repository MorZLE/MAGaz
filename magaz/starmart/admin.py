from django.contrib import admin
from .models import *
# Register your models here.


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo', 'is_published',
                    'Quantity', 'category', 'price')

    list_display_links = ("id", 'title', 'photo')
    search_fields = ('title', 'category', 'price')
    list_editable = ('is_published',)
    list_filter = ("is_published", "price", 'category', 'Quantity')


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'user', 'quantity', 'created_timestamp')
    list_display_links = ('id', 'product', 'user', 'quantity', 'created_timestamp')
    search_fields = ('id', 'product', 'user', 'quantity', 'created_timestamp')


class RecipientDataAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'address', 'number', 'email')
    list_display_links = ('recipient', 'address', 'number', 'email')
    search_fields = ('recipient', 'address', 'number', 'email')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'price', 'quantity')
    list_display_links = ('id', 'order', 'product', 'price', 'quantity')
    search_fields = ('id', 'order', 'product', 'price', 'quantity')


class StatusOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')
    list_display_links = ('id', 'status')
    search_fields = ('id', 'status')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'RecipientData', 'paid', 'status')
    list_display_links = ('id', 'user', 'RecipientData', 'paid', 'status')
    search_fields = ('id', 'user', 'RecipientData', 'paid', 'status')


admin.site.register(Goods, GoodsAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(RecipientData, RecipientDataAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(StatusOrder, StatusOrderAdmin)
admin.site.register(Order, OrderAdmin)

