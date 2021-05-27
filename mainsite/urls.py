from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name="login"),
    path('profil/', views.profil, name="profil"),
    path('community/', views.community, name="community"),
    path('planner/', views.planner, name="planner"),
]
