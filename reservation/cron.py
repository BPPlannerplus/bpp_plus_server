from .models import *
import datetime


def reservation_state_change():
    reservations = Reservation.objects.all()
    for reservation in reservations:
        if reservation.state == Reservation.CONFIRMED and reservation.reserved_date < datetime.date.today():
            reservation.state = Reservation.UNREVIEWED # 예약만료
            reservation.save()
        elif reservation.state == Reservation.UNREVIEWED and reservation.reserved_date + datetime.timedelta(weeks=2) < datetime.date.today():
            reservation.state = Reservation.INVALID # 리뷰작성불가
        elif reservation.state == Reservation.REVIEWED and reservation.reserved_date + datetime.timedelta(weeks=2) < datetime.date.today():
            reservation.review.editable = False # 수정불가


