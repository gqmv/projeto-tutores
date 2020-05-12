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

    author = models.ForeignKey(
        User, null=False, on_delete=models.CASCADE, related_name="appointments_author"
    )
    ad = models.ForeignKey(
        Ad, null=False, on_delete=models.CASCADE, related_name="appointments_ad"
    )

    # scheduled_time = models.DateTimeField()

    is_confirmed = models.BooleanField(default=False)

    objects = models.Manager()

    @property
    def tutor(self):
        if self.ad.ad_type == "T":
            return self.ad.author
        else:
            return self.author

    @property
    def student(self):
        if self.ad.ad_type == "L":
            return self.ad.author
        else:
            return self.author
