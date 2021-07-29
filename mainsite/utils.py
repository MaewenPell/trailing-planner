from mainsite.models import SportProfil
from django.contrib.auth.models import User
from user_profil.db_query import DBQuery


def generate_running_data(sport_profil, trainings):
    context = {
        "sport_profil": sport_profil,
        "trainings": {},
        "all_km": [],
        "all_deniv": [],
    }

    km_done = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0}
    deniv_done = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0}

    for elem in trainings:
        context["trainings"][elem.trainingDateDayStr] = elem
        if elem.status is True:
            km_done[elem.trainingDateDayStr] = elem.trainingKm
            deniv_done[elem.trainingDateDayStr] = elem.trainingD

    for elem in km_done:
        context["all_km"].append(km_done[elem])
    for elem in deniv_done:
        context["all_deniv"].append(deniv_done[elem])

    return context


def get_index_data():
    profils = SportProfil.objects.all()
    ctx = {
        "nb_runners": len(profils),
        "km_ran": 0,
        "elevation_gained": 0
    }
    for user in profils:
        curr_user = DBQuery(User.objects.get(username=user))
        _, user_profil = curr_user.get_user_profil()
        trainings = curr_user.get_all_trainings()
        data = generate_running_data(user_profil, trainings)
        ctx['km_ran'] += sum(data['all_km'])
        ctx['elevation_gained'] += sum(data['all_deniv'])

    return ctx


def get_top_runners():
    profils = SportProfil.objects.all()
    ranking = {
        "all_name": [],
        "all_km": [],
        "first": {
            "name": "",
            "km_ran": 0,
        },
        "second": {
            "name": "",
            "km_ran": 0,
        },
        "third": {
            "name": "",
            "km_ran": 0,
        }
    }
    alls = {}
    for user in profils:
        curr_user = DBQuery(User.objects.get(username=user))
        _, user_profil = curr_user.get_user_profil()
        trainings = curr_user.get_all_trainings()
        data = generate_running_data(user_profil, trainings)

        alls[user.user.first_name] = sum(data['all_km'])

    alls = dict(sorted(alls.items(), key=lambda item: item[1], reverse=True))
    for i, key in enumerate(alls):
        if i == 0:
            ranking["all_name"].append(key)
            ranking["all_km"].append(alls[key])
            ranking["first"]["name"] = key
            ranking['first']['km_ran'] = alls[key]
        elif i == 1:
            ranking["all_name"].append(key)
            ranking["all_km"].append(alls[key])
            ranking["second"]["name"] = key
            ranking['second']['km_ran'] = alls[key]
        elif i == 2:
            ranking["all_name"].append(key)
            ranking["all_km"].append(alls[key])
            ranking["third"]["name"] = key
            ranking["third"]["km_ran"] = alls[key]

    return ranking
