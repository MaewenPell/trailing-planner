from django.shortcuts import render, redirect
from user_profil.db_query import DBQuery


def profil(request):
    if request.user.is_authenticated:
        res, sport_profil = DBQuery(request.user).get_user_profil()
        return render(request, 'profil.html', sport_profil)
    else:
        return redirect("register")


def create_sport_profil(request):
    if request.user.is_authenticated:
        res, sport_profil = DBQuery(request.user).create_user_profil(request.POST)
    return profil(request)
