from django.db import models

# Create your models here.

from login.models import *
from shop.models import *
from multiselectfield import MultiSelectField

COMPLAIN_CHOCIE = (
    ('abuse', '음란, 욕설 등 부적절한 내용'),
    ('ads', '부적절한 홍보 또는 광고 내용'),
    ('privacy', '개인 정보 노출'),
    ('illegal', '불법 정보 기재'),
    ('etc', '기타(직접입력)'),
)

class Review(TimeStampMixin):
    score = models.IntegerField()
    contents = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    editable = models.BooleanField(default=True)


class Complain(TimeStampMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    reason = MultiSelectField(choices=COMPLAIN_CHOCIE)
    contents = models.TextField()

