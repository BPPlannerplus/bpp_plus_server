from django.urls import path
from .views import *

app_name = 'reservation'

urlpatterns = [
    path('', ReservationList.as_view()),  # 예약전체조회
    path('shops/<int:pk>', AddReservation.as_view()),  # shop 예약추가
    path('<int:pk>/reviews/',ReservationReviewDetail.as_view()), # 예약에 대한 리뷰 작성, 조회
    path('<int:pk>', ReservationDetail.as_view()),  # reservation 수정, 취소
    path('states/', ReservationCheck.as_view()) # reservation 상태 체크
]
