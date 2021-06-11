from django.urls import path
from . import views

urlpatterns = [
    path("", views.profil, name="profil"),
    path('sport_profil/', views.create_sport_profil, name="createSportProfil"),
]
