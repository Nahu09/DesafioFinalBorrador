from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from user.views.user import SignUp


urlpatterns = [
    path('', SignUp.as_view(), name="signup_view")
]
