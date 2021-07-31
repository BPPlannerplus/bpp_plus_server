from django.shortcuts import render
from .models import *
from rest_framework.pagination import PageNumberPagination
from .serializers import *
# apiview
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication


def getUser(request):
    JWT_authenticator = JWTAuthentication()
    response = JWT_authenticator.authenticate(request)
    if response is not None:
        user, token = response
        return user
    else:
        return Response(status=400, data={ 'error': "no token is provided in the header or the header is missing"})


class AddReservation(APIView):
    def post(self, request, pk, format=None):
        shop = Shop.objects.get(id=pk)
        reservation = Reservation(state=Reservation.INQUIRY, reserved_date=None, user=getUser(request), shop= shop)
        reservation.save()
        return Response(status=200)

class ReservationList(APIView, PageNumberPagination):
    def get(self, request, format=None):
        user = getUser(request)
        reservations = user.reservation_set.all().order_by('-pk')

        self.page_size = 10
        page_result = self.paginate_queryset(reservations, request, view=self)
        serializer = ReservationSerializer(page_result, many=True)
        return Response(serializer.data)


class ReservationDetail(APIView):
    pass
    # # 특정모델을 찾아주고 없다면 404에러 발생시켜줄 함수
    # def get_object(self, pk):
    #     try:
    #         return Post.objects.get(pk=pk)
    #     except Post.DoesNotExist:
    #         raise Http404
    #
    # def post(self, request, format=None):
    #     serializer = PostSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    #
    # def patch(self, request, pk, format=None):
    #     post = self.get_object(pk)
    #     serializer = PostSerializer(post, data=request.data, partial= True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk, format=None):
    #     post = self.get_object(pk)
    #     post.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)