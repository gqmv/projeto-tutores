from rest_framework import serializers

from general.models import Appointment

from django.contrib.auth.models import User


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    tutor = serializers.HyperlinkedRelatedField(many=False, view_name="api-user-detail", read_only=True)

    class Meta:
        model = Appointment
        fields = ["id", "tutor", "price", "subject"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    appointments_tutor = serializers.HyperlinkedRelatedField(many=True, view_name="api-appointment-detail", read_only=True)

    class Meta:
        model = User
        fields = ["username", "id", "appointments_tutor"]
