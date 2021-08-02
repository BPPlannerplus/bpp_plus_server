from django.db import models
from login.models import *
#from reservation.models import *

class Shop(TimeStampMixin):
    STUDIO = 0 #0 대신 SHOP.STUDIO로 쓰기위해
    BEAUTYSHOP = 1
    SHOP_TYPE_CHOICES = (
        (STUDIO, 'studio'),
        (BEAUTYSHOP, 'beautyshop'),
    )

    ADDRESS_CHOICES = (
        ('gangnam','강남구'),
        ('gangdong','강동구'),
        ('gwangjin','광진구'),
        ('mapo','마포구'),
        ('seocho','서초구')
    )

    name = models.CharField(max_length=20)
    address = models.CharField(max_length = 20,choices=ADDRESS_CHOICES)
    address_detail = models.TextField(max_length=50)
    minprice = models.IntegerField()

    price_desc = models.ImageField(blank=True, null=True)
    profile = models.ImageField(blank=True, null=True)  # 컨셉중에서 대표사진1
    profile_2 = models.ImageField(blank=True, null=True)  # 컨셉중에서 대표사진2
    profile_3 = models.ImageField(blank=True, null=True)  # 컨셉중에서 대표사진3
    map = models.ImageField(blank=True, null=True) #지도
    kakaourl = models.URLField(blank=True, null=True)
    logo = models.ImageField(blank=True, null=True)
    shop_type = models.IntegerField(choices=SHOP_TYPE_CHOICES)  # 0 : studio, 1 : beautyshop
    like_users = models.ManyToManyField(User,through='LikeShop',related_name="like_shops", blank=True, null=True)
    like_count = models.IntegerField(default=0)
    #pick_users = models.ManyToManyField(User, through='Reservation', related_name="pick_shops") #reservation에 중개모델
    affiliates = models.ManyToManyField('self',symmetrical=True, blank=True, null=True) #제휴업체 대칭적 관계로

    def __str__(self):
        return self.name

class LikeShop(TimeStampMixin):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE)
