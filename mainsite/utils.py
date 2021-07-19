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
