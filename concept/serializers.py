from rest_framework import serializers
from .models import *


# StudioConceptSerializer에서 shop 일부 정보만 표시용
class StudioConceptShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name')


# studio_concept 전체 목록(컨셉북) 조회
class StudioConceptSerializer(serializers.ModelSerializer):
    like = serializers.SerializerMethodField('is_like') # user가 특정 concept에 찜을 했는지

    class Meta:
        model = StudioConcept
        fields = ('id', 'profile', 'shop', 'like')

    def is_like(self, obj): # user가 특정 concept에 찜을 했는지
        if LikeStudioConcept.objects.filter(studio_concept=obj.id, user=self.context['user'].id):
            return True
        else:
            return False

    def to_representation(self, instance): # shop의 id랑 이름만 전달
        response = super().to_representation(instance)
        response['shop'] = StudioConceptShopSerializer(instance.shop).data
        return response


# ShopDetailConcept에서 StudioConcept 일부 정보만 표시용
class OneStudioConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudioConcept
        fields = ('id', 'profile')


# ShopDetailConcept에서 BeautyShopConcept 일부 정보만 표시용
class OneBeautyShopConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeautyShopConcept
        fields = ('id', 'profile')
