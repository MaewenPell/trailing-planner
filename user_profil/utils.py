def generate_running_data_profil(sport_profil, trainings):
    context = {
        "sport_profil": sport_profil,
        "trainings": {},
        "all_km": [],
        "all_deniv": [],
        "labels": [i for i in range(0, 32)]
    }

    km_done = {}
    deniv_done = {}

    for i in range(0, 31):
        km_done[str(i)] = 0
        deniv_done[str(i)] = 0

    for elem in trainings:
        context["trainings"][elem.trainingDate.day] = elem
        if elem.status is True:
            km_done[str(elem.trainingDate.day)] = elem.trainingKm
            deniv_done[str(elem.trainingDate.day)] = elem.trainingD

    for elem in km_done:
        context["all_km"].append(km_done[elem])
    for elem in deniv_done:
        context["all_deniv"].append(deniv_done[elem])

    return context


def get_all_trainings_data(all_trainings):
    list_all_trainings = {
        "km": [],
        "deniv": [],
        "total_km": 0,
        "total_d": 0,
        "nb_trainings": 0,
    }
    for training in all_trainings:
        list_all_trainings["km"].append(training.trainingKm)
        list_all_trainings["deniv"].append(training.trainingD)

    list_all_trainings["nb_trainings"] = len(
        list_all_trainings["km"])
    list_all_trainings["total_d"] = sum(list_all_trainings["deniv"])
    list_all_trainings["total_km"] = sum(list_all_trainings["km"])

    return list_all_trainings
