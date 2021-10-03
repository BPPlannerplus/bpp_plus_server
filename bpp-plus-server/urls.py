from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shops/', include('shop.urls')),
    path('login/', include('login.urls')),
    path('concepts/', include('concept.urls')),
    path('reservations/', include('reservation.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
