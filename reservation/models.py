from django.db import *
from login.models import *
from shop.models import *
from cs.models import *


class Reservation(TimeStampMixin):
    INQUIRY = 0  # 0 대신 RESERVATION.INQUIRY로 접근하기 위해
    CONFIRMED = 1
    REVIEWED = 2
    UNREVIEWED = 3

    STATE_CHOICES = (
        (INQUIRY, 'inquiry'),
        (CONFIRMED, 'confirmed'),
        (REVIEWED, 'reviewed'),
        (UNREVIEWED, 'unreviewed'),
    )

    state = models.IntegerField(null=False, blank=False, choices=STATE_CHOICES)  # 0 : 문의중 , 1 : 예약확정, 2 : 리뷰완료, 3: 리뷰없이
    reserved_date = models.DateField(null=True, blank=True) # 예약확정날짜(문의중일때는 null로)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    review = models.OneToOneField(Review, on_delete= models.SET_NULL, null=True, blank=True)
