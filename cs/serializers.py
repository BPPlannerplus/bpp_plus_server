from rest_framework import serializers
from .models import *
from login.models import *

# OneShopReviewSerializer에서 user에 필요한 정보만 표시하기 위해
class OneUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class OneReviewSerializer(serializers.ModelSerializer):

     class Meta:
        model = Review
        fields = "__all__"


class OneShopReviewSerializer(serializers.ModelSerializer):
    reserved_user = serializers.SerializerMethodField('user')

    class Meta:
        model = Review
        fields = ("id", "reserved_user", "score", "contents", "date")

    def user(self, obj):
        return obj.reservation.user.username
