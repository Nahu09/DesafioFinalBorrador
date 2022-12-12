from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from login.views.login import Login, AdminLogoutView


urlpatterns = [
    path('', Login.as_view(), name="login_view"),
    path('signup/', include('user.urls')),
    path('logout/', AdminLogoutView.as_view(), name="logout_view")
]
