from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# admin 패널에서 User를 보고 싶어서 등록을 하는 것이고,
# User를 컨트롤 할 class를 CustomUserAdmin으로 선언해봤어 입니다.
@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','uid','username','exp','refresh','created_at', 'updated_at')
    list_display_links = ('id','uid','username','exp','refresh', 'created_at', 'updated_at')