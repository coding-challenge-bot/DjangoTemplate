from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home_page.urls')),
    path('password/', include('password_generator.urls')),
]
