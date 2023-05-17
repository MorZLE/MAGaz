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


admin.site.register(Goods, GoodsAdmin)
admin.site.register(Categories, CategoriesAdmin)

