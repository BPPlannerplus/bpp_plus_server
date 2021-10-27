from rest_framework.decorators import APIView
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from login.views import get_user
import json


class ReviewList(APIView, PageNumberPagination):
    def get(self, request, pk):
        self.page_size = 20
        reviews = Review.objects.filter(shop=pk)
        result_page = self.paginate_queryset(reviews, request, view=self)
        serializer = OneShopReviewSerializer(result_page, many=True, context={"request": request})

        return self.get_paginated_response(serializer.data)

    def post(self, request, pk):
        user = get_user(request)
        score = json.loads(request.body.decode('utf-8')).get('score')
        contents = json.loads(request.body.decode('utf-8')).get('contents')
        Review.objects.create(user=user.id, shop=pk, score=score, contents=contents)

        return Response(status=status.HTTP_201_CREATED)



class ReviewDetail(APIView):
    def get(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        serialzer = OneReviewSerializer(review, context={"request": request})

        return Response(data=serialzer.data)

# 삭제 + 수정 



class ComplainDetail(APIView):
    def post(self, request, pk):
        user = get_user(request)
        reason = json.loads(request.body.decode('utf-8')).get('reason')
        contents = json.loads(request.body.decode('utf-8')).get('contents')
        Complain.objects.create(user=user.id, review=pk, reason= reason, contents=contents)

        return Response(status=status.HTTP_201_CREATED)


