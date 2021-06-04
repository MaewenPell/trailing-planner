from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('create-new-user/', views.createNewUser, name="createNewUser"),
    path('login/', views.login, name="login"),
    path('login-user/', views.loginUser, name="connectUser"),
]
