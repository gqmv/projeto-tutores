from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("appointments/all", views.AppointmentList, name="appointments-list"),
    path("appointments/<int:pk>/", views.AppointmentDetail, name="appointments-detail"),
    path("appointments/new/", views.AppointmentNew, name="appointments-new"),
]
