from django.urls import path
from . import views

urlpatterns = [
    path("", views.cv_index, name="cv_index"),
]