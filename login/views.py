from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.shortcuts import get_object_or_404
from rest_auth.registration.views import SocialLoginView
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import SocialLoginSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
import secrets
import string
from .models import *
import datetime
from django.utils import timezone
import os,environ



env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# reading .env file
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

char_string = string.ascii_letters + string.digits

def getRandomString(size):
    return ''.join(secrets.choice(char_string) for _ in range(size))


# access token으로 user정보 알아내기 
def get_user(request):
    JWT_authenticator = JWTAuthentication()
    response = JWT_authenticator.authenticate(request)  # request안에 access token을 이용해서 user객체와 token 추출 
    if response is not None:
        user, token = response
        return user   
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data={"error": "no token is provided in the header or the header is missing"})
    
    
@api_view(['POST'])
def new_token(request):
    # request에 있는 access_token값
    access_token = json.loads(request.body.decode('utf-8')).get('access_token')

    # POST이면서 request에 access_token이 있을때
    if request.method == 'POST' and access_token != None:
        url = "http://localhost:8000/login/rest-auth/kakao/"
        headers = {'Content-Type': 'application/json'}
        data = {"access_token": access_token}
        response = requests.post(url, headers=headers, data=json.dumps(data))

        if response.status_code == status.HTTP_200_OK:
            uid = response.json()['user']['uid']  #kakao가 넘겨준 정보중 uid빼오기 
            new_body = json.loads(requests.post(
                'http://localhost:8000/login/token/', data={"uid": uid, "password": env("PASSWORD")}).content)  # jwt 토큰생성
            user = get_object_or_404(User, uid=uid)
            user.refresh = getRandomString(200)  # secure random string -> refresh token 
            user.exp = datetime.datetime.now() + datetime.timedelta(days=7)  # refresh 유효기간 저장 
            user.save()
            new_body["refresh"] = user.refresh  # refresh token 수정
            return Response(new_body)  # secure random string refreash , access token 전달
        else:
            return Response({"detail": "kakao response status code is not 200","status":response.status_code, "response":response.text}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"detail": "access_token not exist"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def refresh_token(request):
    # body에 있는 refresh_token값
    refresh_token = json.loads(request.body.decode('utf-8')).get('refresh_token')
    user_id = json.loads(request.body.decode('utf-8')).get('user_id')

    user = get_object_or_404(User, id=user_id)
    if refresh_token == user.refresh:

        if user.exp > timezone.now():  # 유효할때
            new_body = json.loads(requests.post(
                'http://localhost:8000/login/token/', data={"uid": user.uid, "password": env("PASSWORD")}).content)  # jwt 토큰생성
            del new_body['refresh']  # refresh token 제거
            return Response(new_body)

        else:  # 만료되었을 때
            msg = {'error message': 'refresh token is expired'}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)

    else:  # refresh token 일치하지 않을 때
        msg = {'error message': 'refresh token is mismatched'}
        return Response(msg, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def withdraw(request):
    user = get_user(request)
    User.objects.filter(id=user.id).delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter
    client_class = OAuth2Client
    serializer_class = SocialLoginSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
