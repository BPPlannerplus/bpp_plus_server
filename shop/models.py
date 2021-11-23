from django.db import models
from login.models import *
from .validators import validate_file_size

class Shop(TimeStampMixin):
    STUDIO = 0  # 0 대신 SHOP.STUDIO로 쓰기위해
    BEAUTYSHOP = 1  # 1 대신 SHOP.BEAUTYSHOP로 쓰기위해
    WAXINGSHOP = 2 # 2 대신 SHOP.WAXINGSHOP으로 쓰기위해
    TANNINGSHOP = 3 # 3 대신 SHOP.TANNINGSHOP으로 쓰기위해
    SHOP_TYPE_CHOICES = (
        (STUDIO, 'studio'),
        (BEAUTYSHOP, 'beautyshop'),
        (WAXINGSHOP, 'waxingshop'),
        (TANNINGSHOP, 'tanningshop'),

    )

    ADDRESS_CHOICES = (
        ('gangnam', '강남구'),
        ('gangdong', '강동구'),
        ('gwangjin', '광진구'),
        ('mapo', '마포구'),
        ('seocho', '서초구'),
        ('yangchun', '양천구')
    )

    name = models.CharField(max_length=100)  # shop 이름
    address = models.CharField(max_length=100, choices=ADDRESS_CHOICES)  # 주소에서 구(강남,강동,...)
    address_detail = models.TextField(max_length=100)  # 전체주소
    minprice = models.IntegerField(null=True,blank=True)  # 최소가격

    price_desc = models.ImageField(null=True,blank=True,validators=[validate_file_size])  # 가격설명 사진
    price_desc_extra = models.ImageField(null=True,blank=True,validators=[validate_file_size]) # 가격설명 여분
    profile = models.ImageField(validators=[validate_file_size])  # 대표사진1
    profile_2 = models.ImageField(validators=[validate_file_size])  # 대표사진2
    profile_3 = models.ImageField(validators=[validate_file_size])  # 대표사진3
    map = models.ImageField(validators=[validate_file_size])  # 지도(약도)사진
    kakaourl = models.URLField()  # 카카오url
    logo = models.ImageField(validators=[validate_file_size])  # 로고사진
    shop_type = models.IntegerField(choices=SHOP_TYPE_CHOICES)  # 0 : studio, 1 : beautyshop
    like_users = models.ManyToManyField(User, through='LikeShop', related_name="like_shops", blank=True,
                                        null=True)  # 찜한 user들
    like_count = models.PositiveIntegerField(default=0)  # 찜수
    affiliates = models.ManyToManyField('self', symmetrical=True, blank=True, null=True)  # 제휴업체 대칭적 관계로

    def __str__(self):
        return self.name


class LikeShop(TimeStampMixin):  # Shop에서 like_users 필드에 through
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
