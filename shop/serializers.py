from rest_framework import serializers
from .models import *
from concept.serializers import *


# shop 전체 목록
class ShopSerializer(serializers.ModelSerializer):
    like = serializers.SerializerMethodField('is_like')  # user가 특정 shop에 찜을 했는지

    class Meta:
        model = Shop
        fields = ('id', 'name', 'address', 'minprice', 'profile', 'like')

    def is_like(self, obj):  # user가 특정 shop에 찜을 했는지
        if LikeShop.objects.filter(shop=obj.id, user=self.context['user'].id):
            return True
        else:
            return False


# OneShopSerializer에서 협력업체 일부 정보만 표시용
class AffiliateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'profile')


# shop 세부정보
class OneShopSerializer(serializers.ModelSerializer):
    affiliates = AffiliateSerializer(read_only=True, many=True)  # 협력업체들
    like = serializers.SerializerMethodField('is_like')  # user가 특정 shop에 찜을 했는지
    profiles = serializers.SerializerMethodField('profile_array')  # 대표사진 3개 묶어서 array로 전달

    class Meta:
        model = Shop
        fields = (
            'id', 'name', 'address_detail', 'minprice', 'price_desc', 'price_desc_extra', 'logo', 'profiles', 'map', 'kakaourl', 'affiliates','like',
        )

    def is_like(self, obj):  # user가 특정 shop에 찜을 했는지
        if LikeShop.objects.filter(shop=obj.id, user=self.context['user'].id):
            return True
        else:
            return False

    def profile_array(self, obj):  # 대표사진 3개 묶어서 array로 전달
        return [self.context['request'].build_absolute_uri(obj.profile.url),
                self.context['request'].build_absolute_uri(obj.profile_2.url),
                self.context['request'].build_absolute_uri(obj.profile_3.url)]
