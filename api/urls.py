from django.contrib import admin
from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r"appointments", views.AppointmentViewSet)
router.register(r"users", views.UserViewSet)
urlpatterns = [
    path("auth/", include("rest_framework.urls"), name="api-auth"),
    path("", include(router.urls)),
]
