from django.db import models
from django.contrib.auth.models import User
from . import presets


class Appointment(models.Model):
    tutor = models.ForeignKey(
        User, null=False, on_delete=models.CASCADE, related_name="appointments_tutor"
    )
    student = models.ForeignKey(
        User, null=False, on_delete=models.CASCADE, related_name="appointments_student"
    )
    subject = models.CharField(max_length=3, choices=presets.AVAILIBLE_SUBJECTS)
    scheduled_time = models.DateTimeField()
    price = models.PositiveIntegerField()

    objects = models.Manager()
