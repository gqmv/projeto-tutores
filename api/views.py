from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework import status

from general.models import Appointment, Ad
from .serializers import AppointmentSerializer, UserSerializer, AdSerializer
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


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permissions = [custom_permissions.IsOwnerOrReadOnly]

    def update(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TutorAdViewSet(AdViewSet):
    queryset = Ad.objects.all().filter(ad_type="T")


class StudentAdViewSet(AdViewSet):
    queryset = Ad.objects.all().filter(ad_type="L")
