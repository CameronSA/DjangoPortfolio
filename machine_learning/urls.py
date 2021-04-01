from django.urls import path
from . import views

urlpatterns = [
    path("", views.machine_learning_index, name="machine_learning_index"),
    path("supervised/", views.supervised_learning_index, name="supervised_learning_index"),
    path("unsupervised/", views.unsupervised_learning_index, name="unsupervised_learning_index"),
]