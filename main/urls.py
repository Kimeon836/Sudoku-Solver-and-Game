from argparse import Namespace
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("check/", views.check, name="check"),
    path("get_steps/", views.get_steps, name="get_steps"),
]