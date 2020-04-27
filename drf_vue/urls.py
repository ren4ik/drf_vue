from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/chat/', include("chat.urls")),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]
