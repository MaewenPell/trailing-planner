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
    trainingDateWeekNb = models.IntegerField(default=0)
    trainingDateMonthNb = models.CharField(max_length=20, default="")
    trainingDateYearNb = models.IntegerField(default=2021)
    trainingDateDayStr = models.CharField(default="0", max_length=3)
    trainingType = models.CharField(max_length=40, default="")
    trainingKm = models.IntegerField(default=0)
    trainingD = models.IntegerField(default=0)
    trainingComments = models.CharField(max_length=200, default="")
    status = models.BooleanField(default=False)
    feeling = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.trainingType} from the {self.trainingDate}"

    class Meta:
        ordering = ["trainingDate"]
