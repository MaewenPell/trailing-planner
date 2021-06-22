from django.shortcuts import render, redirect
from user_profil.db_query import DBQuery


def index(request):
    return render(request, 'index.html')


def wallOfFame(request):
    return render(request, 'walloffame.html')


def planner(request):
    _, sport_profil = DBQuery(request.user).get_user_profil()
    if request.user.is_authenticated:
        return render(request, 'planner.html', sport_profil)
    else:
        return redirect("register")


def addNewTraining(request):
    return render(request, 'add_training.html')


def createNewTraining(request):
    if request.user.is_authenticated:
        DBQuery(request.user).create_training(request.POST)
        return redirect("add_new_training")
    else:
        redirect("register")
