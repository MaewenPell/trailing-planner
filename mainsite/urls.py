from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('walloffame/', views.wallOfFame, name="walloffame"),
    path('planner/', views.planner, name="planner"),
    path('addnewtraining/', views.addNewTraining, name="add_new_training"),
    path('createnewtraining/',
         views.createNewTraining, name="create-new-training")
]
