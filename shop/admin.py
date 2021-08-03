from django.contrib import admin
from .models import *


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'shop_type',
    )

    list_display_links = (
        'id',
        'name',
        'shop_type',
    )


@admin.register(LikeShop)
class LikeShopAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'shop',
    )

    list_display_links = (
        'user',
        'shop',
    )
