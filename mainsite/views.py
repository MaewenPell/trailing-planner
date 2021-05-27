from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def profil(request):
    return render(request, 'profil.html')


def community(request):
    return render(request, 'community.html')


def planner(request):
    return render(request, 'planner.html')
