from django.conf.urls import url
from django.urls import path

from . import views
# from .views import ActivateAccount

urlpatterns = [
    path("register", views.register, name="register"),
    path("login",views.login, name="login"),
    path("logout",views.logout,name="logout"),
    # path("bloodd",views.bloodd,name="blood"),

    path("view_profile", views.view_profile, name="view_profile"),


    ]
