from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class SportProfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, unique=True)
    strava_link = models.CharField(max_length=200, default="")
    final_objectif_name = models.CharField(max_length=200, default="")
    final_objectif_date = models.DateField(
        "Final objectif date", default=timezone.now)
    final_objectif_deniv = models.IntegerField(default=0)
    final_objectif_km = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.user}"
