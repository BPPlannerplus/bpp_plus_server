from django.urls import path
from .views import *

app_name = 'cs'

urlpatterns = [
    path('shops/<int:pk>', ReviewList.as_view()),  # 특정 shop 리뷰전체조회, 추가
    path('<int:pk>', ReviewDetail.as_view()),  # 특정 리뷰 조회, 삭제, 수정
    path('<int:pk>/complains/', ComplainList.as_view()) # 특정 리뷰에 신고추가
]