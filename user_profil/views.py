from django.shortcuts import render, redirect
from user_profil.db_query import DBQuery
from user_profil.utils import generate_running_data_profil
from datetime import datetime


def profil(request):
    if request.user.is_authenticated:
        Curr_user = DBQuery(request.user)
        _, sport_profil = Curr_user.get_user_profil()

        month_trainings = Curr_user.get_month_trainings(
            datetime.now().strftime("%b")
        )
        context = generate_running_data_profil(sport_profil, month_trainings)

        return render(request, 'profil.html', context)
    else:
        return redirect("register")


def create_sport_profil(request):
    if request.user.is_authenticated:
        res, sport_profil = DBQuery(
            request.user).create_sport_profil(request.POST)
    return profil(request)
