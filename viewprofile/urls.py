from django.urls import path

from . import views

urlpatterns = [
    #automobile//////
    path("vh1<int:pk>", views.vh1, name="vh1"),
    path("vh2<int:pk>", views.vh2, name="vh2"),
    path("vh3<int:pk>", views.vh3, name="vh3"),
    path("vh4<int:pk>", views.vh4, name="vh4"),
    path("vh5<int:pk>", views.vh5, name="vh5"),
    path("vh6<int:pk>", views.vh6, name="vh6"),
    path("vh7<int:pk>", views.vh7, name="vh7"),
    path("vh8<int:pk>", views.vh8, name="vh8"),
    path("vh9<int:pk>", views.vh9, name="vh9"),
    path("vh10<int:pk>", views.vh10, name="vh10"),
    #doctor//////////
    path("vd1<int:pk>", views.vd1, name="vd1"),
    path("vd2<int:pk>", views.vd2, name="vd2"),
    path("vd3<int:pk>", views.vd3, name="vd3"),
    path("vd4<int:pk>", views.vd4, name="vd4"),
    #////hotel
    path("vh<int:pk>", views.vh, name="vh"),
    #////resturnts
    path("vr<int:pk>", views.vr, name="vr"),
    #////electricians
    path("ve<int:pk>", views.ve, name="ve"),
    #////automobiles
    path("va1<int:pk>", views.va1, name="va1"),
    path("va2<int:pk>", views.va2, name="va2"),
    path("va3<int:pk>", views.va3, name="va3"),
    path("va4<int:pk>", views.va4, name="va4"),
    path("va5<int:pk>", views.va5, name="va5"),
    #///////plumber
    path("vp1<int:pk>", views.vp1, name="vp1"),
    path("vp2<int:pk>", views.vp2, name="vp2"),
    path("vp3<int:pk>", views.vp3, name="vp3"),
    path("vp4<int:pk>", views.vp4, name="vp4"),





]