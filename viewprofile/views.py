from django.shortcuts import render

# Create your views here.
from Webapp.models import hospital
from Webapp.models import childhospital
from Webapp.models import eyehospital
from Webapp.models import publichospital
from Webapp.models import ENThospital
from Webapp.models import privatehospital
from Webapp.models import cancerhospital
from Webapp.models import mentalhospital
from Webapp.models import multisuperhospital
from Webapp.models import orthrohospital
from Webapp.models import carrepair
from Webapp.models import cartyres
from Webapp.models import carwash
from Webapp.models import caracesseries
from Webapp.models import motercyclerepair
from Webapp.models import dentists
from Webapp.models import eye
from Webapp.models import bone
from Webapp.models import dentists
from Webapp.models import dermatology
from Webapp.models import plumbercont
from Webapp.models import plumberproducts
from Webapp.models import plumberinstall
from Webapp.models import plumberservice
from Webapp.models import electrician
from Webapp.models import hotel
from Webapp.models import reasurant






#//////////hospitals profileview ///////////
def vh1(request, pk=None):
        v = hospital.objects.get(pk=pk)
        return render(request, 'profile.html', {'v': v})
def vh2(request, pk=None):
    v = childhospital.objects.get(pk=pk)
    return render(request, 'profile.html', {'v': v})
def vh3(request, pk=None):
    v = eyehospital.objects.get(pk=pk)
    return render(request, 'profile.html', {'v': v})
def vh4(request, pk=None):
    v = publichospital.objects.get(pk=pk)
    return render(request, 'profile.html', {'v': v})
def vh5(request, pk=None):
    v = ENThospital.objects.get(pk=pk)
    return render(request, 'profile.html', {'v': v})
def vh6(request, pk=None):
    v =privatehospital.objects.get(pk=pk)
    return render(request, 'profile.html', {'v': v})
def vh7(request, pk=None):
    v = cancerhospital.objects.get(pk=pk)
    return render(request, 'profile.html', {'v': v})
def vh8(request, pk=None):
    v = mentalhospital.objects.get(pk=pk)
    return render(request, 'profile.html', {'v': v})
def vh9(request, pk=None):
    v =multisuperhospital.objects.get(pk=pk)
    return render(request, 'profile.html', {'v': v})
def vh10(request, pk=None):
    v = orthrohospital.objects.get(pk=pk)
    return render(request, 'profile.html', {'v': v})
#/////////////////doctor view /////////
def vd1(request, pk=None):
    v = dentists.objects.get(pk=pk)
    return render(request, 'profile.html', {'v': v})
def vd2(request, pk=None):
    v = eye.objects.get(pk=pk)
    return render(request, 'profile.html', {'v': v})
def vd3(request, pk=None):
    v = dermatology.objects.get(pk=pk)
    return render(request, 'profile.html', {'v': v})
def vd4(request, pk=None):
    v = bone.objects.get(pk=pk)
    return render(request, 'profile.html', {'v': v})
#///////hotels
def vh(request, pk=None):
    v = hotel.objects.get(pk=pk)
    return render(request, 'profile.html', {'v': v})
#//////resturents
def vr(request, pk=None):
    v = reasurant.objects.get(pk=pk)
    return render(request, 'profile.html', {'v': v})
#//////electricians
def ve(request, pk=None):
    v =electrician.objects.get(pk=pk)
    return render(request, 'profile.html', {'v': v})
#/////automobiles
def va1(request, pk=None):
    v =electrician.objects.get(pk=pk)
    return render(request, 'profile.html', {'v': v})
def va2(request, pk=None):
    v =electrician.objects.get(pk=pk)
    return render(request, 'profile.html', {'v': v})
def va3(request, pk=None):
    v =electrician.objects.get(pk=pk)
    return render(request, 'profile.html', {'v': v})
def va4(request, pk=None):
    v =electrician.objects.get(pk=pk)
    return render(request, 'profile.html', {'v': v})
def va5(request, pk=None):
    v =electrician.objects.get(pk=pk)
    return render(request, 'profile.html', {'v': v})
#///////plumber
def vp1(request, pk=None):
    v =plumberservice.objects.get(pk=pk)
    return render(request, 'profile.html', {'v': v})
def vp2(request, pk=None):
    v =plumberproducts.objects.get(pk=pk)
    return render(request, 'profile.html', {'v': v})

def vp3(request, pk=None):
    v =plumbercont.objects.get(pk=pk)
    return render(request, 'profile.html', {'v': v})

def vp4(request, pk=None):
    v =plumberinstall.objects.get(pk=pk)
    return render(request, 'profile.html', {'v': v})








