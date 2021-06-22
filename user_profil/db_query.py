from user_profil.models import SportProfil
from mainsite.models import Training, TrainingResume, SportProfil
from django.contrib.auth.models import User
from datetime import date


class DBQuery():
    def __init__(self, user) -> None:
        self.user = user

    def create_sport_profil(self, sport_profil) -> tuple:
        self.objectif_name = sport_profil['objectifName']
        self.objectif_distance = sport_profil['objectifDistance']
        self.objectif_d = sport_profil['objectifD']
        self.objectif_date = sport_profil['objectifDate']
        year = int(self.objectif_date[:4])
        month = int(self.objectif_date[5:7])
        day = int(self.objectif_date[8:10])
        self.stravaLink = sport_profil['stravaLink']

        curr_user = User.objects.get(username=self.user.username)

        new_sport_profil = SportProfil.objects.create(
            user=curr_user,
            strava_link=self.stravaLink,
            final_objectif_name=self.objectif_name,
            final_objectif_date=date(
                year=year, month=month, day=day),
            final_objectif_deniv=self.objectif_d,
            final_objectif_km=self.objectif_distance
        )
        return (True, new_sport_profil)

    def get_user_profil(self) -> tuple:
        try:
            sport_profil_user = SportProfil.objects.get(user=self.user)
            context = {
                'user': {
                    'first_name': sport_profil_user.user.first_name,
                    'last_name': sport_profil_user.user.last_name,
                    'email': sport_profil_user.user.email,
                    'username': sport_profil_user.user.username,
                },
                'final_objectif_name': sport_profil_user.final_objectif_name,
                'final_objectif_km': sport_profil_user.final_objectif_km,
                'final_objectif_deniv': sport_profil_user.final_objectif_deniv,
                'final_objectif_date': sport_profil_user.final_objectif_date,
            }
            return (True, context)
        except SportProfil.DoesNotExist:
            return (False, None)

    def create_training(self, new_training):
        training_res, created = TrainingResume.objects.get_or_create(
            sportProfilRelated=SportProfil.objects.get(user=self.user)

        )
        training_date = new_training['trainingDate']
        year = int(training_date[:4])
        month = int(training_date[5:7])
        day = int(training_date[8:10])
        Training.objects.create(
            trainingListResume=training_res,
            trainingDate=date(year=year, month=month, day=day),
            trainingType=new_training['trainingType'],
            trainingKm=new_training['trainingKm'],
            trainingD=new_training['trainingD'],
            trainingComments=new_training['trainingComments'],
            status=False,
            feeling=0,
        )
