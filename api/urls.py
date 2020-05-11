from django.contrib import admin
from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("appointments/", views.Appointments.as_view(), name="appointments-list"),
    path("appointments/<int:pk>/", views.AppointmentDetail.as_view(), name="appointments-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
