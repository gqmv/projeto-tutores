from rest_framework import serializers

from general import models

from django.contrib.auth.models import User


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    tutor = serializers.HyperlinkedRelatedField(
        many=False, view_name="user-detail", read_only=True
    )
    student = serializers.HyperlinkedRelatedField(
        many=False, view_name="user-detail", read_only=True
    )
    ad = serializers.HyperlinkedRelatedField(
        many=False, view_name="ad-detail", read_only=True
    )

    class Meta:
        model = models.Appointment
        fields = ["id", "tutor", "student", "price", "subject"]


class AdSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        many=False, view_name="user-detail", read_only=True
    )

    class Meta:
        model = models.Ad
        fields = ["id", "author", "price", "subject", "is_availible", "ad_type"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    appointments_tutor = serializers.HyperlinkedRelatedField(
        many=True, view_name="appointment-detail", read_only=True
    )

    class Meta:
        model = User
        fields = ["username", "id", "appointments_tutor"]
