from django.shortcuts import render, redirect
from user_management.users import CreateNewUser, ConnectUser
from django.contrib import messages


def register(request):
    return render(request, 'register.html')


def createNewUser(request):
    if request.POST:
        res, msg, _ = CreateNewUser(request.POST).register()
        if res:
            return redirect("index")
        else:
            for message in msg:
                messages.error(request, message)
            return redirect("register")


def login(request):
    return render(request, 'login.html')


def loginUser(request):
    res, msg = ConnectUser(request.POST).connect(request)
    if res:
        return redirect('index')
    else:
        messages.error(request, msg)
        return redirect("login")
