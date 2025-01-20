from django.contrib import admin

from .models import Buyer, Auto


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')
    list_filter = ('name', 'age')
    search_fields = ('name',)
    list_per_page = 20


@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'year')  # для отображения полей
    list_filter = ('name', 'color')  # для фильтрации
    search_fields = ('name',)  # для поиска
    list_per_page = 30  # количество элементов на странице
    readonly_fields = ('color',)
