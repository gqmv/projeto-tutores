from django.contrib import admin
from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("", views.api_root, name="api-root"),

    path("auth/", include("rest_framework.urls"), name="api-auth"),

    path("appointments/", views.Appointments.as_view(), name="api-appointments"),
    path(
        "appointments/<int:pk>/",
        views.AppointmentDetail.as_view(),
        name="api-appointment-detail",
    ),
    
    path("users/", views.Users.as_view(), name="api-users"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="api-user-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
