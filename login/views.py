from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
#from rest_auth.registration.serializers import SocialLoginSerializer
from rest_auth.registration.views import SocialLoginView
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import SocialLoginSerializer,MyTokenObtainPairSerializer,CustomUserDetailsSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
import secrets
import string
from .models import *
import datetime


char_string = string.ascii_letters + string.digits

def getRandomString(size):
    return ''.join(secrets.choice(char_string) for _ in range(size))


@api_view(['POST'])
def new_tokens(request):
    # request에 있는 access_token값
    access_token = json.loads(request.body.decode('utf-8')).get('access_token')
    
    # POST이면서 request에 access_token이 있을때
    if request.method == 'POST' and access_token != None:
        url = "http://localhost:8000/login/rest-auth/kakao/"
        headers = {'Content-Type': 'application/json'}
        data = {"access_token": access_token}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        
        if response.status_code == 200:
            uid = response.json()['user']['uid']
            new_body = json.loads(requests.post(
                'http://localhost:8000/login/token/', data={"uid": uid, "password":"1234"}).content) # jwt 토큰생성
            user = User.objects.get(uid=uid)
            print(user)
            user.refresh = getRandomString(24)  # secure random string
            user.exp = datetime.datetime.now() + datetime.timedelta(days=7)
            user.save()
            new_body["refresh"] = user.refresh   # refresh token 수정
            return Response(new_body) # secure random string refreash , access token 전달

    return Response(status=400)



@api_view(['POST'])
def refresh_token(request):
    # body에 있는 refresh_token값
    refresh_token = json.loads(request.body.decode('utf-8')).get('refresh_token')

    JWT_authenticator = JWTAuthentication()
    response = JWT_authenticator.authenticate(request)
    if response is not None:
        user, token = response
        print("this is decoded token claims", token.payload)
        return Response(status=200)
    else:
        print("no token is provided in the header or the header is missing")

    return Response(status=400)



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