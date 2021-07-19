from django.shortcuts import render, redirect
from user_profil.db_query import DBQuery
from mainsite.utils import generate_running_data
import datetime


def index(request):
    return render(request, 'index.html')


def wallOfFame(request):
    return render(request, 'walloffame.html')


def planner(request):
    if request.user.is_authenticated:
        Curr_user = DBQuery(request.user)
        _, sport_profil = Curr_user.get_user_profil()
        trainings = Curr_user.get_week_trainings(
            datetime.date.today().isocalendar()[1])

        context = generate_running_data(sport_profil, trainings)

        return render(request, 'planner.html', context)
    else:
        return redirect("register")


def addNewTraining(request):
    return render(request, 'add_training.html')


def createNewTraining(request):
    if request.user.is_authenticated:
        DBQuery(request.user).create_training(request.POST)
        return redirect("planner")
    else:
        redirect("register")


def trainingDone(request):
    if request.user.is_authenticated:
        DBQuery(request.user).update_training(request.POST)
        return redirect("planner")
