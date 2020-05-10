from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Appointment
from .serializers import AppointmentSerializer


@api_view(["GET"])
def AppointmentList(request):
    appointments = Appointment.objects.all()
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data)
