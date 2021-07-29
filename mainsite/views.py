from django.shortcuts import render, redirect
from user_profil.db_query import DBQuery
from mainsite.utils import generate_running_data
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
from mainsite.utils import get_index_data, get_top_runners


def index(request):
    ctx = get_index_data()
    return render(request, 'index.html', ctx)


def wallOfFame(request):
    ctx = get_top_runners()
    return render(request, 'walloffame.html', ctx)


def planner(request):
    if request.user.is_authenticated:
        Curr_user = DBQuery(request.user)
        _, sport_profil = Curr_user.get_user_profil()
        trainings = Curr_user.get_week_trainings(
            date.today().isocalendar()[1])

        context = generate_running_data(sport_profil, trainings)

        return render(request, 'planner.html', context)
    else:
        return redirect("register")


def addNewTraining(request):
    first_day = (
        datetime.today() - timedelta(
            days=datetime.today().weekday() % 7)
        )
    last_day = first_day + relativedelta(days=6)

    context = {
        "first_day": first_day.strftime("%Y-%m-%d"),
        "last_day": last_day.strftime("%Y-%m-%d"),
    }

    return render(request, 'add_training.html', context)


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
