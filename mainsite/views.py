from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def wallOfFame(request):
    return render(request, 'walloffame.html')


def planner(request):
    return render(request, 'planner.html')
