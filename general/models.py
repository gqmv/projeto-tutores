from django.db import models
from django.contrib.auth.models import User
from . import presets


class Ad(models.Model):
    author = models.ForeignKey(
        User, null=False, on_delete=models.CASCADE, related_name="ads"
    )
    subject = models.CharField(max_length=3, choices=presets.AVAILIBLE_SUBJECTS)
    price = models.PositiveIntegerField()
    ad_type = models.CharField(max_length=1, choices=presets.AD_TYPES)

    is_availible = models.BooleanField(default=True)

    objects = models.Manager()


class Appointment(models.Model):
    tutor = models.ForeignKey(
        User, null=False, on_delete=models.CASCADE, related_name="appointments_tutor"
    )
    student = models.ForeignKey(
        User, null=False, on_delete=models.CASCADE, related_name="appointments_student"
    )
    ad = models.ForeignKey(
        Ad, null=False, on_delete=models.CASCADE, related_name="appointments_ad"
    )

    subject = models.CharField(max_length=3, choices=presets.AVAILIBLE_SUBJECTS)
    # scheduled_time = models.DateTimeField()
    price = models.PositiveIntegerField()

    is_confirmed = models.BooleanField(default=False)

    objects = models.Manager()
