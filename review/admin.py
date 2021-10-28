from django.contrib import admin
from .models import *


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'shop', 'score', 'contents', 'date')
    list_display_links = ('id', 'user', 'shop', 'score', 'contents', 'date')


@admin.register(Complain)
class ComplainAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'review', 'reason', 'contents')
    list_display_links = ('id', 'user', 'review', 'reason', 'contents')
