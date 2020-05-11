from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets

from general.models import Appointment
from .serializers import AppointmentSerializer, UserSerializer
from . import permissions as custom_permissions

from django.contrib.auth.models import User


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permissions = [custom_permissions.IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(tutor=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
