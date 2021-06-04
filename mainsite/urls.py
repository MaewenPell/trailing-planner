from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profil/', views.profil, name="profil"),
    path('walloffame/', views.wallOfFame, name="walloffame"),
    path('planner/', views.planner, name="planner"),
]
