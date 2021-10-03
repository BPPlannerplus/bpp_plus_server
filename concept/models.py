from django.db import models
from django.db.models.enums import Choices
from multiselectfield import MultiSelectField
from shop.models import *
from login.models import *
from .validators import validate_file_size
# CHOICES(https://pypi.org/project/django-multiselectfield/)
HEAD_COUNT_CHOICES = (
    (1, '1인'),
    (2, '2인'),
    (3, '3인이상'),
)
GENDER_CHOICES = (
    ('man', '남성'),
    ('woman', '여성'),
)
BACKGROUND_CHOICES = (
    ('white', '흰색'),
    ('black', '검은색'),
    ('chromatic', '유채색'),
    ('etc', '기타배경'),
    ('outside', '야외'),
)
PROP_CHOICES = (
    ('health', '헬스도구'),
    ('mini', '소가구'),
    ('etc', '기타소품'),
    ('none','없음'),
)
DRESS_CHOICES = (
    ('athleisure', '애슬레저'),
    ('swimsuit', '수영복'),
    ('underwear', '언더웨어'),
    ('etc', '기타')
)


class StudioConcept(TimeStampMixin):
    profile = models.ImageField(validators=[validate_file_size]) #concept 사진
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="studio_concepts") #어떤 shop의 concept인지
    like_users = models.ManyToManyField(User, through='LikeStudioConcept', related_name="like_studio_concepts", null=True, blank=True) #찜한 user들
    like_count = models.PositiveIntegerField(default=0) #찜수

    head_count = MultiSelectField(choices=HEAD_COUNT_CHOICES) #인원
    gender = MultiSelectField(choices=GENDER_CHOICES) #성별
    background = MultiSelectField(choices=BACKGROUND_CHOICES) #배경
    prop = MultiSelectField(choices=PROP_CHOICES) #소품
    dress = MultiSelectField(choices=DRESS_CHOICES) #의상

    def __str__(self):
        return self.shop.name + '의 스튜디오컨셉' +'(id: '+str(self.id)+')'


class LikeStudioConcept(TimeStampMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    studio_concept = models.ForeignKey(StudioConcept, on_delete=models.CASCADE)


class BeautyShopConcept(TimeStampMixin): #beautyshop_concept에는 찜 없다
    profile = models.ImageField(validators=[validate_file_size])
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="beautyshop_concepts")

    def __str__(self):
        return self.shop.name + '의 뷰티샵컨셉'+'(id: '+str(self.id)+')'
