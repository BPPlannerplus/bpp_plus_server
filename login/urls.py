from django.urls import path
from .views import *

app_name = 'login'

urlpatterns = [
    path('rest-auth/kakao/', KakaoLogin.as_view(), name='kakao_login'),
    path('new-token/', new_token.as_view(), name='new_tokens'),  # kakao access token -> access, refresh token
    path('token/refresh/', refresh_token, name='token_refresh'),  # 재발급 api
    path('withdrawal/', withdraw, name='withdrawal'),  # 회원탈퇴
]
