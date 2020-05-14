from rest_framework import serializers

from general import models

from django.contrib.auth.models import User


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        many=False, view_name="user-detail", read_only=True
    )
    tutor = serializers.HyperlinkedRelatedField(
        many=False, view_name="user-detail", read_only=True
    )
    student = serializers.HyperlinkedRelatedField(
        many=False, view_name="user-detail", read_only=True
    )

    ad = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    class Meta:
        model = models.Appointment
        fields = ["id", "author", "ad", "tutor", "student", "is_confirmed"]


class AppointmentSerializerPOST(AppointmentSerializer):
    ad = serializers.PrimaryKeyRelatedField(
        queryset=models.Ad.objects.all(), required=True
    )

    class Meta:
        model = models.Appointment
        fields = ["id", "author", "ad", "tutor", "student", "is_confirmed"]


class AdSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        many=False, view_name="user-detail", read_only=True
    )

    class Meta:
        model = models.Ad
        fields = ["id", "author", "price", "subject", "is_availible", "ad_type"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username", "id"]
