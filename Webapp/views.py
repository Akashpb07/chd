from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib import messages

from .models import Destination, hotel
from .models import automobile
from .models import dentists
from .models import plumbercont
from .models import plumberinstall
from .models import plumberproducts
from .models import plumberservice
from .models import reasurant
from .models import blooddonor
from .models import hospital
from .models import childhospital
from Webapp.models import eyehospital
from Webapp.models import publichospital
from Webapp.models import ENThospital
from Webapp.models import privatehospital
from Webapp.models import cancerhospital
from Webapp.models import mentalhospital
from Webapp.models import multisuperhospital
from Webapp.models import orthrohospital
from .models import carrepair
from Webapp.models import cartyres
from Webapp.models import carwash
from Webapp.models import caracesseries
from Webapp.models import motercyclerepair
from .models import bone
from .models import eye
from .models import dermatology
from .models import electrician
from .models import Requestaddservice
# Create your views here.

def viewprofile(request, pk=None):
    if pk:
        v = dentists.objects.get(pk=pk)
    else:
        v = request.dentists
    return render(request, 'profile.html', {'v': v})



def bloodd(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        gender= request.POST['gender']
        blood_group = request.POST['bg']
        mobile_no = request.POST['mobileno']
        address = request.POST['address']
        city = request.POST['city']
        if blooddonor.objects.filter(mobile_no=mobile_no).exists():
            messages.info(request, 'Mobile Number Alredy Taken')
            return redirect('db')
        elif blooddonor.objects.filter(email=email).exists():
            messages.info(request, 'Email Taken')
            return redirect('db')
        else:
            x = blooddonor(name=name,email=email ,age=age ,gender=gender ,blood_group=blood_group ,mobile_no=mobile_no ,address=address ,city=city)
            x.save()
            return redirect('table')
    else:
        return render(request,"db")

def adds(request):
    if request.method == 'POST':
        Category = request.POST['cat']
        Name = request.POST['fn']
        Speciality = request.POST['sp']
        Department= request.POST['dp']
        Address = request.POST['ad']
        ServiceDescription = request.POST['des']
        img = request.POST['img']
        # Ownername = request.POST['n']
        # Ownermobno= request.POST['mb']
        x = Requestaddservice(Category=Category,Name=Name ,Speciality =Speciality  ,Department=Department ,Address=Address , ServiceDescription= ServiceDescription ,img=img )
        x.save()
        return redirect('adddone')
    else:
        return render(request,"addservice.html")


# ////////////////index page
def index(request):
    return render(request, "index.html")
def test(request):
    return render(request,"forgotpassword.html")
#/////////////add Services page/////
def addservices(request):
    return  render(request,"addservice.html")
def adddone(request):
    return  render(request,"adddone.html")
# ///////////1st All  pages
def doctor(request):
    return  render(request,"doctors.html")

def resutrants(request):
    pss = reasurant.objects.all()
    return render(request, "reasurants/reasurants.html", {'pss': pss})


def plumbers(request):
    return  render(request,"plumber.html")

def ele(request):
    pss = electrician.objects.all()
    return render(request, "electricians/electricians.html", {'pss': pss})


def automobiles(request):
    return render(request,"automobile.html")
def hotels(request):
    pss = hotel.objects.all()
    return render(request, "hotels/hotels.html", {'pss': pss})


def hospitals(request):
    return  render(request,"hospitals.html")

def aboutus(request):
    return render(request, "about.html")

def contactus(request):
    return render(request, "contact.html")
def blooddonate(request):
    return render(request,"blood.html")
#///blood table
def table(request):
    pss=blooddonor.objects.all()
    return render(request,"blood/table.html" ,{'pss':pss})

#///////////blood Donate////////////
def db(request):
    return render(request, "blood/blooddonate.html")
def fb(request):
    return render(request, "blood/findblood.html")


class SearchResultsView(ListView):
    model = blooddonor
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list =blooddonor.objects.filter(
           Q(blood_group__icontains=query)
        )
        return object_list

#/////////////////doctor speciality
def d1(request):
    dens = dentists.objects.all()
    return render(request, "dr/denist.html", {'dens': dens})
def d2(request):
    dens = eye.objects.all()
    return render(request, "dr/eye.html", {'dens': dens})
def d3(request):
    dens = dermatology.objects.all()
    return render(request, "dr/dermatology.html", {'dens': dens})
def d4(request):
    dens = bone.objects.all()
    return render(request, "dr/bone.html", {'dens': dens})



#///////////////////////plumber services
def pservice(request):
    pss = plumberservice.objects.all()
    return render(request,"plumbers/plumber1.html",{'pss': pss})
def pproduct(request):
    pss = plumberproducts.objects.all()
    return render(request, "plumbers/plumber2.html", {'pss': pss})
def pcontractors(request):
    dens = plumbercont.objects.all()
    return render(request,"plumbers/plumber3.html",{'dens': dens})
def pinstalltion(request):
    dens = plumberinstall.objects.all()
    return render(request,"plumbers/plumber4.html",{'dens': dens})


#////////////Hospitals////////

def h1(request):
    pss = hospital.objects.all()
    return render(request, "hospitals/h1.html", {'pss': pss})



def h2(request):
    pss = childhospital.objects.all()
    return render(request, "hospitals/h2.html", {'pss': pss})



def h3(request):
    pss = eyehospital.objects.all()
    return render(request, "hospitals/h3.html", {'pss': pss})


def h4(request):
    pss = publichospital.objects.all()
    return render(request, "hospitals/h4.html", {'pss': pss})



def h5(request):
    pss = ENThospital.objects.all()
    return render(request, "hospitals/h5.html", {'pss': pss})



def h6(request):
    pss = privatehospital.objects.all()
    return render(request, "hospitals/h6.html", {'pss': pss})



def h7(request):
    pss = cancerhospital.objects.all()
    return render(request, "hospitals/h7.html", {'pss': pss})



def h8(request):
    pss = mentalhospital.objects.all()
    return render(request, "hospitals/h8.html", {'pss': pss})



def h9(request):
    pss = multisuperhospital.objects.all()
    return render(request, "hospitals/h9.html", {'pss': pss})



def h10(request):
    pss = orthrohospital.objects.all()
    return render(request, "hospitals/h10.html", {'pss': pss})

#/////////////automobile all uls?/////////

def a1(request):
    pss = carrepair.objects.all()
    return render(request, "automobile/a1.html", {'pss': pss})
def a2(request):
    pss = caracesseries.objects.all()
    return render(request, "automobile/a2.html", {'pss': pss})
def a3(request):
    pss = carwash.objects.all()
    return render(request, "automobile/a3.html", {'pss': pss})
def a4(request):
    pss = cartyres.objects.all()
    return render(request, "automobile/a4.html", {'pss': pss})
def a5(request):
    pss = motercyclerepair.objects.all()
    return render(request, "automobile/a5.html", {'pss': pss})










