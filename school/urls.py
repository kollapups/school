from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home),
    path("oauth/login/", views.oauth_login),
    path("oauth/callback/", views.oauth_callback),
]
