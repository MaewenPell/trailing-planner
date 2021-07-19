def generate_running_data_profil(sport_profil, trainings):
    context = {
        "sport_profil": sport_profil,
        "trainings": {},
        "all_km": [],
        "all_deniv": [],
        "labels": [i for i in range(0, 31)]
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
