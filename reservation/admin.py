from django.contrib import admin
from .models import *


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id','user','shop','state','reserved_date', 'review')
    list_display_links = ('id','user','shop','state','reserved_date', 'review')