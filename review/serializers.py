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

    class Meta:
        model = Review
        fields = ("id", "user", "score", "contents", "date")

    def to_representation(self, instance):  # user에서 필요한 정보만 표시
        response = super().to_representation(instance)
        response["user"] = OneUserSerializer(instance.user, context={"request": self.context['request']}).data
        return response
