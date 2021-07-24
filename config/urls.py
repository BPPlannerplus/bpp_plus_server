from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shop.urls')),
    path('login/', include('login.urls')),
    path('concepts/',include('concept.urls')),
    path('reservations/',include('reservation.urls')),
]


