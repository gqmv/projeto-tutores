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

@api_view(["GET"])
def AppointmentDetail(request, pk):
    appointments = Appointment.objects.get(id=pk)
    serializer = AppointmentSerializer(appointments, many=False)
    return Response(serializer.data)

@api_view(["POST"])
def AppointmentNew(request):
    serializer = AppointmentSerializer(request.data)

    if serializer.is_valid:
        serializer.save()

    return Response(serializer.data)