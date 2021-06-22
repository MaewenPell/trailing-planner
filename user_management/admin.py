from django.contrib import admin
from user_profil.models import SportProfil
from mainsite.models import TrainingResume, Training


# Register your models here.
admin.site.register(SportProfil)
admin.site.register(TrainingResume)
admin.site.register(Training)
