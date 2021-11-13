from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
from .views import *

app_name = 'login'

urlpatterns = [
    path('rest-auth/kakao/', KakaoLogin.as_view(), name='kakao_login'),
    path('new-token/', new_token.as_view(), name='new_tokens'),  # kakao access token -> access, refresh token
    path('token/refresh/', refresh_token, name='token_refresh'),  # 재발급 api
    path('withdrawal/', withdraw, name='withdrawal'),  # 회원탈퇴

    # simple jwt
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),  # access , refresh token 발급
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # 유효성검증 api
]
