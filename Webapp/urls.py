from django.urls import path

from . import views
from .views import SearchResultsView

urlpatterns = [
    #/////////index page //
    path("", views.index, name="index"),

    path("viewprofile<int:pk>", views.viewprofile, name="viewprofile"),

    path("add", views.addservices, name="addservices"),

    #//////////services Urls
    path("contactus",views.contactus, name="contactus"),
    path("doctor", views.doctor, name="doctor"),
    path("resutrants", views.resutrants, name="resutrants"),
    path("plumbers", views.plumbers, name="plumber"),
    path("electrician", views.ele, name="electrician"),
    path("automobiles", views.automobiles, name="automobile"),
    path("hotels", views.hotels, name="hostels"),
    path("hospitals", views.hospitals, name="hospitals"),
    path("blood", views.blooddonate, name="blood"),
    path("bloodd", views.bloodd, name="bloodd"),
    path("table", views.table, name="table"),
    path("adddone", views.adddone, name="adddone"),
    path("adds",views.adds, name="adds"),




    #//////donate blood////
    path("db", views.db, name="db"),
    path("fb", views.fb, name="fb"),
    path('search/', SearchResultsView.as_view(), name='search_results'),


    #//////////doctor urls
    path("d1", views.d1, name="d1"),
    path("d3", views.d3, name="d3"),
    path("d4", views.d4, name="d4"),
    path("d2", views.d2, name="d2"),


    #//////////autombile url
    path("a1",views.a1 , name="a1"),
    path("a2",views.a2 , name="a2"),
    path("a3",views.a3 , name="a3"),
    path("a4",views.a4 , name="a4"),
    path("a5",views.a5 , name="a5"),

    #//////////plumbing urls
    path("pservice", views.pservice, name="pservice"),
    path("pproduct", views.pproduct, name="pproduct"),
    path("pcontractors", views.pcontractors, name="pcontractors"),
    path("pinstalltion", views.pinstalltion, name="pinstalltion"),


    # //////////Hospitals urls
    path("h1", views.h1),
    path("h2", views.h2),
    path("h3", views.h3),
    path("h4", views.h4),
    path("h5", views.h5),
    path("h6", views.h6),
    path("h7", views.h7),
    path("h8", views.h8),
    path("h9", views.h9),
    path("h10", views.h10),

















               ]

