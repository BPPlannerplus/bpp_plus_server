from .models import *
import datetime


def reservation_state_change():
    reservations = Reservation.objects.all()
    for reservation in reservations:
        if reservation.state == Reservation.CONFIRMED and reservation.reserved_date < datetime.date.today():
            reservation.state = Reservation.UNREVIEWED
            reservation.save()

def test():
    print("hello")
    