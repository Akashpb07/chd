from django.db import models

# Create your models here.


class Destination(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

#/////////////automobile/////
class automobile(models.Model):
    drimg = models.ImageField(upload_to="drpics")
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    location = models.TextField()
    mobNo = models.CharField(max_length=15)
    def __str__(self):
        return self.name
#/////////////doctor/////
class dentists(models.Model):
    drimg = models.ImageField(upload_to="denistsdoctors")
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    deprtimg = models.ImageField(upload_to="denistsdoctors")
    department = models.CharField(max_length=100)
    location = models.TextField(max_length=100)
    mobNo = models.CharField(max_length=15)
    def __str__(self):
        return self.name
class eye(models.Model):
    drimg = models.ImageField(upload_to="drpics")
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    deprtimg = models.ImageField(upload_to="drpics")
    department = models.CharField(max_length=100)
    location = models.TextField(max_length=100)
    mobNo = models.CharField(max_length=15)
    def __str__(self):
        return self.name
class bone(models.Model):
    drimg = models.ImageField(upload_to="drpics")
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    deprtimg = models.ImageField(upload_to="drpics")
    department = models.CharField(max_length=100)
    location = models.TextField(max_length=100)
    mobNo = models.CharField(max_length=15)
    def __str__(self):
        return self.name
class dermatology(models.Model):
    drimg = models.ImageField(upload_to="drpics")
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    deprtimg = models.ImageField(upload_to="drpics")
    department = models.CharField(max_length=100)
    location = models.TextField(max_length=100)
    mobNo = models.CharField(max_length=15)
    def __str__(self):
        return self.name

#///////////plumber services//////////

class plumberservice(models.Model):
    drimg = models.ImageField(upload_to="plumber-s")
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    deprtimg = models.ImageField(upload_to="plumber-s")
    department = models.CharField(max_length=100)
    location = models.TextField(max_length=100)
    mobNo = models.CharField(max_length=15)
    def __str__(self):
        return self.name



class plumberproducts(models.Model):
    drimg = models.ImageField(upload_to="plumber-p")
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    deprtimg = models.ImageField(upload_to="plumber-p")
    department = models.CharField(max_length=100)
    location = models.TextField(max_length=100)
    mobNo = models.CharField(max_length=15)
    def __str__(self):
        return self.name


class plumbercont(models.Model):
    drimg = models.ImageField(upload_to="plumber-c")
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    deprtimg = models.ImageField(upload_to="plumber-c")
    department = models.CharField(max_length=100)
    location = models.TextField(max_length=100)
    mobNo = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class plumberinstall(models.Model):
    drimg = models.ImageField(upload_to="plumber-i")
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    deprtimg = models.ImageField(upload_to="plumber-i")
    department = models.CharField(max_length=100)
    location = models.TextField(max_length=100)
    mobNo = models.CharField(max_length=15)
    def __str__(self):
        return self.name
#////////////electricians///////////////

class electrician(models.Model):
    drimg = models.ImageField(upload_to="plumber-i")
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    deprtimg = models.ImageField(upload_to="plumber-i")
    department = models.CharField(max_length=100)
    location = models.TextField(max_length=100)
    mobNo = models.CharField(max_length=15)
    def __str__(self):
        return self.name
#/////////////////hotels/////////////////

class hotel(models.Model):
    drimg = models.ImageField(upload_to="plumber-i")
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    deprtimg = models.ImageField(upload_to="plumber-i")
    department = models.CharField(max_length=100)
    location = models.TextField(max_length=100)
    mobNo = models.CharField(max_length=15)
    def __str__(self):
        return self.name
#///////////////reasurant///////////////////

class reasurant(models.Model):
    drimg = models.ImageField(upload_to="plumber-i")
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    deprtimg = models.ImageField(upload_to="plumber-i")
    department = models.CharField(max_length=100)
    location = models.TextField(max_length=100)
    mobNo = models.CharField(max_length=15)
    def __str__(self):
        return self.name




#/////////////hospitals Models///////////

class hospital(models.Model):
    drimg = models.ImageField(upload_to="hospital")
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    deprtimg = models.ImageField(upload_to="hospital")
    department = models.CharField(max_length=100)
    location = models.TextField(max_length=100)
    mobNo = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class childhospital(models.Model):
    drimg = models.ImageField(upload_to="childhospital")
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    deprtimg = models.ImageField(upload_to="childhospital")
    department = models.CharField(max_length=100)
    location = models.TextField(max_length=100)
    mobNo = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class eyehospital(models.Model):
    drimg = models.ImageField(upload_to="eyehospital")
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    deprtimg = models.ImageField(upload_to="eyehospital")
    department = models.CharField(max_length=100)
    location = models.TextField(max_length=100)
    mobNo = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class publichospital(models.Model):
    drimg = models.ImageField(upload_to="publichospital")
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    deprtimg = models.ImageField(upload_to="publichospital")
    department = models.CharField(max_length=100)
    location = models.TextField(max_length=100)
    mobNo = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class privatehospital(models.Model):
     drimg = models.ImageField(upload_to="privatehospital")
     name = models.CharField(max_length=100)
     speciality = models.CharField(max_length=100)
     deprtimg = models.ImageField(upload_to="privatehospital")
     department = models.CharField(max_length=100)
     location = models.TextField(max_length=100)
     mobNo = models.CharField(max_length=15)

     def __str__(self):
         return self.name

class ENThospital(models.Model):
    drimg = models.ImageField(upload_to="ENThospital")
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    deprtimg = models.ImageField(upload_to="ENThospital")
    department = models.CharField(max_length=100)
    location = models.TextField(max_length=100)
    mobNo = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class cancerhospital(models.Model):
    drimg = models.ImageField(upload_to="cancerhospital")
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    deprtimg = models.ImageField(upload_to="cancerhospital")
    department = models.CharField(max_length=100)
    location = models.TextField(max_length=100)
    mobNo = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class mentalhospital(models.Model):
    drimg = models.ImageField(upload_to="mentalhospital")
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    deprtimg = models.ImageField(upload_to="mentalhospital")
    department = models.CharField(max_length=100)
    location = models.TextField(max_length=100)
    mobNo = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class multisuperhospital(models.Model):
    drimg = models.ImageField(upload_to="multisuperhospital")
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    deprtimg = models.ImageField(upload_to="multisuperhospital")
    department = models.CharField(max_length=100)
    location = models.TextField(max_length=100)
    mobNo = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class orthrohospital(models.Model):
    drimg = models.ImageField(upload_to="othrohospital")
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    deprtimg = models.ImageField(upload_to="othrohospital")
    department = models.CharField(max_length=100)
    location = models.TextField(max_length=100)
    mobNo = models.CharField(max_length=15)
    def __str__(self):
        return self.name

    #////////////////Automobile /////////////
class newcars(models.Model):
    drimg = models.ImageField(upload_to="automobile")
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    deprtimg = models.ImageField(upload_to="automobile")
    department = models.CharField(max_length=100)
    location = models.TextField(max_length=100)
    mobNo = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class carrepair(models.Model):
    drimg = models.ImageField(upload_to="automobile")
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    deprtimg = models.ImageField(upload_to="automobile")
    department = models.CharField(max_length=100)
    location = models.TextField(max_length=100)
    mobNo = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class caracesseries(models.Model):
    drimg = models.ImageField(upload_to="automobile")
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    deprtimg = models.ImageField(upload_to="automobile")
    department = models.CharField(max_length=100)
    location = models.TextField(max_length=100)
    mobNo = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class carwash(models.Model):
    drimg = models.ImageField(upload_to="automobile")
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    deprtimg = models.ImageField(upload_to="automobile")
    department = models.CharField(max_length=100)
    location = models.TextField(max_length=100)
    mobNo = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class cartyres(models.Model):
    drimg = models.ImageField(upload_to="automobile")
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    deprtimg = models.ImageField(upload_to="automobile")
    department = models.CharField(max_length=100)
    location = models.TextField(max_length=100)
    mobNo = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class motercyclerepair(models.Model):
    drimg = models.ImageField(upload_to="automobile")
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    deprtimg = models.ImageField(upload_to="automobile")
    department = models.CharField(max_length=100)
    location = models.TextField(max_length=100)
    mobNo = models.CharField(max_length=15)
    def __str__(self):
        return self.name


#///////////blood donate//////#
class blooddonor(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    age=models.IntegerField()
    gender=models.CharField(max_length=20)
    blood_group=models.CharField(max_length=20)
    mobile_no=models.CharField(max_length=15)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)

    class Meta:
      verbose_name_plural = " Blood Donations"

    def __str__(self):
        return self.name




#/////////Add services model//////
class Requestaddservice(models.Model):
    Category =models.CharField(max_length=100)
    Name =models.CharField(max_length=50)
    Speciality =models.CharField(max_length=50)
    Department =models.CharField(max_length=20)
    Address=models.TextField(max_length=200)
    ServiceDescription =models.TextField(max_length=200)
    img =models.ImageField(upload_to='req add')
    Ownername =models.CharField(max_length=50)
    Ownermobno =models.CharField(max_length=15)

    def __str__(self):
        return self.Category






