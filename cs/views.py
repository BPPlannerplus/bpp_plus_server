from rest_framework.decorators import APIView
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from login.views import get_user
from reservation.models import Reservation
import json


class ReviewList(APIView, PageNumberPagination):
    def get(self, request, pk):
        self.page_size = 20
        reviews = Review.objects.filter(reservation__shop=pk).order_by('id')
        result_page = self.paginate_queryset(reviews, request, view=self)
        serializer = OneShopReviewSerializer(result_page, many=True, context={"request": request})

        return self.get_paginated_response(serializer.data)





# 특정리뷰 수정
class ReviewDetail(APIView):
    def patch(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        serializer = OneReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ComplainList(APIView):
    def post(self, request, pk):
        user = get_user(request)
        reason = json.loads(request.body.decode('utf-8')).get('reason')
        contents = json.loads(request.body.decode('utf-8')).get('contents')
        Complain.objects.create(user=user.id, review=pk, reason= reason, contents=contents)

        return Response({"result":"create complain"}, status=status.HTTP_201_CREATED)


