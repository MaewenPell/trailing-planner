from django.db import models
from django.utils import timezone
from user_profil.models import SportProfil


class TrainingResume(models.Model):
    sportProfilRelated = models.ForeignKey(
        SportProfil, on_delete=models.CASCADE, default=None
    )
    totalKm = models.IntegerField(default=0)
    totalD = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"Week : {self.sportProfilRelated}"


class Training(models.Model):
    trainingListResume = models.ForeignKey(
        TrainingResume, on_delete=models.CASCADE)
    trainingDate = models.DateField(
        "Date of training", default=timezone.now)
    trainingType = models.CharField(max_length=40, default="")
    trainingKm = models.IntegerField(default=0)
    trainingD = models.IntegerField(default=0)
    trainingComments = models.CharField(max_length=200, default="")
    status = models.BooleanField(default=False)
    feeling = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"Training date : {self.trainingDate}"
