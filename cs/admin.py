from django.contrib import admin
from .models import *


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'score', 'contents', 'date', 'shop', 'user')
    list_display_links = ('id', 'score', 'contents', 'date', 'shop', 'user')

    def shop(self, obj):
        return obj.reservation.shop.id

    def user(self, obj):
        return obj.reservation.user.id


@admin.register(Complain)
class ComplainAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'review', 'reason', 'contents')
    list_display_links = ('id', 'user', 'review', 'reason', 'contents')
