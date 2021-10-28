from django.shortcuts import get_object_or_404
from rest_framework.decorators import APIView
from rest_framework.pagination import PageNumberPagination
import json
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from concept.serializers import *
from .models import *
from login.views import get_user


# studio 혹은 beautyshop 전체 목록
class ShopList(APIView, PageNumberPagination):
    def get(self, request, request_shop_type):
        if request_shop_type == "studios":  # studio 전체목록 조회
            shop_type = Shop.STUDIO
        elif request_shop_type == "beautyshops":  # beautyshop 전체목록 조회
            shop_type = Shop.BEAUTYSHOP
        else:  # url잘못입력
            return Response(status=status.HTTP_404_NOT_FOUND)

        # like parameter 따로 없으면 false로
        # like = request.query_params.get('like', 'false')
        # if like == 'true':
        #     shops = user.like_shops.all()  # user가 찜한 shop들
        # else:  # TODO 여기서 쿼리개선필요


        # request parameter의 address가져오기(없다면 빈문자열로 가져오기)
        address = request.query_params.get('address', '')
        if address:
            shops = Shop.objects.filter(shop_type=shop_type, address=address).order_by('-like_count')  # 좋아요수 내림차순으로
        else:
            shops = Shop.objects.filter(shop_type=shop_type).order_by('-like_count')  # 좋아요수 내림차순으로

        self.page_size = 20
        result_page = self.paginate_queryset(shops, request, view=self)
        serializer = ShopSerializer(result_page, many=True, context={"request": request})
        return self.get_paginated_response(serializer.data)


# 특정 shop에 찜 추가,제거
class ShopLike(APIView):
    def put(self, request, pk):
        shop = get_object_or_404(Shop, pk=pk)  # 어떤 shop에 like할지
        user = get_user(request)  # access_token에서 user 누군지 꺼내기

        change_to_like = json.loads(request.body.decode('utf-8')).get('change_to_like')  # true or false 받기

        if change_to_like == True:
            if LikeShop.objects.filter(shop=shop, user=user):  # 찜객체 이미 존재하면
                return Response({"detail": "already like exist"}, status=status.HTTP_400_BAD_REQUEST)

            LikeShop.objects.create(shop=shop, user=user)  # 찜객체 만들기
            shop.like_count += 1  # shop의 찜수 증가
            return Response({"result": "shop like create"}, status=status.HTTP_201_CREATED)

        elif change_to_like == False:
            like_shop = get_object_or_404(LikeShop, shop=shop, user=user)  # 제거할 찜객체(찜객체 애초에 없으면 404)
            like_shop.delete()  # 찜객체 제거
            shop.like_count -= 1  # shop의 찜수 감소
            return Response(status=status.HTTP_204_NO_CONTENT)

        else:
            return Response({"detail": "key should be true or false"}, status=status.HTTP_400_BAD_REQUEST)


# 특정 shop 조회(concept만 빼고)
class ShopDetail(APIView):
    def get(self, request, pk):
        shop = get_object_or_404(Shop, pk=pk)  # 어떤 shop 조회할지
        user = get_user(request)  # access_token에서 user 누군지 꺼내기

        serializer = OneShopSerializer(shop, context={"request": request, "user": user})
        return Response(serializer.data)


# 특정 shop의 concept들 조회
class ShopDetailConcept(APIView, PageNumberPagination):
    def get(self, request, pk):
        shop = get_object_or_404(Shop, pk=pk)  # 어떤 shop 조회할지
        if shop.shop_type == Shop.STUDIO:  # shop이 studio일때
            concepts = shop.studio_concepts.all()
        else:  # shop이 beautyshop일때
            concepts = shop.beautyshop_concepts.all()  # beautyshop_concept은 찜없어서 찜순 정렬 불가->그냥 등록순으로

        self.page_size = 20
        result_page = self.paginate_queryset(concepts, request, view=self)
        if shop.shop_type == Shop.STUDIO:  # shop이 studio일때
            serializer = OneStudioConceptSerializer(result_page, many=True, context={"request": request})
        else:  # shop이 beautyshop일때
            serializer = OneBeautyShopConceptSerializer(result_page, many=True, context={"request": request})
        return self.get_paginated_response(serializer.data)


