from email.policy import default
from posixpath import split
from re import S
from django.shortcuts import render
from django.http import HttpResponse
from .models import donated_medicine,user_query,user_registration,requested_medicine,user_login


# Create your views here.

def index(request):
    return render(request, 'umdsite/index.html')

def about(request):
    return render(request, 'umdsite/about.html')

def contact(request):
    if request.method=="POST":
        print(request)
        cont_name = request.POST.get('name','')
        cont_email = request.POST.get('email','')
        cont_query = request.POST.get('query','')
        contact= user_query(name=cont_name,email=cont_email,query=cont_query)
        contact.save()
        return HttpResponse('''Queried Successfully <br><a href="/umdsite/contact">go Back</a>''')

    return render(request, 'umdsite/contact.html')

def login(request):
    logn_uname = request.POST.get('UserName')
    logn_pass = request.POST.get('PassWord')
    rl_name=user_registration.objects.all()

    list_users=['aman','vikas','shiv','ritesh','abc']
    for user in list_users:
        if(logn_uname==user and logn_pass!=0):
            return render(request,'umdsite/UserProfile.html')
    
    print(logn_uname)
    return render(request, 'umdsite/login.html')

def register(request):
    if request.method=="POST":
        print(request)
        regt_name = request.POST.get('name')
        regt_cont = request.POST.get('contact_no')
        regt_city = request.POST.get('city_name')
        regt_pincode = request.POST.get('pincode')
        regt_uname = request.POST.get('username')
        regt_pass = request.POST.get('password')
        register=user_registration(full_name=regt_name,phone_no=regt_cont,city=regt_city,pincode=regt_pincode,user_name=regt_uname,pass_key=regt_pass)
        register.save()
        return HttpResponse('''Registered Successfully <br><a href="/umdsite/login">go Back</a>''')

    return render(request, 'umdsite/register.html')

def donation(request):
    if request.method=="POST":
        print(request)
        dont_uname = request.POST.get('username')
        dont_mname = request.POST.get('MedName')
        dont_mDtl = request.POST.get('medDetails')
        dont_add = request.POST.get('address')
        donation=donated_medicine(user_name=dont_uname,med_name=dont_mname,med_details=dont_mDtl,user_address=dont_add)
        donation.save()
        return HttpResponse('''Generate Certificate<br><a href="/umdsite/certificate">certificate</a>''')
    return render(request, 'umdsite/donation.html')

def request(request):
    if request.method=="POST":
        print(request)
        reqt_uname = request.POST.get('username')
        reqt_fname = request.POST.get('FullName')
        reqt_mname = request.POST.get('MedName')
        reqt_add = request.POST.get('address')
        request=requested_medicine(user_name=reqt_uname,full_name=reqt_fname,med_name=reqt_mname,user_address=reqt_add)
        request.save()
        return HttpResponse('''Action completed <br><a href="/umdsite/UserProfile">go Back</a>''')
    a=donated_medicine.objects.all()
    params={'avl_med':list(a)} 
    return render(request, 'umdsite/request.html',params)

def UserProfile(request):
    return render(request, 'umdsite/UserProfile.html')

def VolunteerLogin(request):
    vol_uname = request.POST.get('volunteer-choice')
    vol_pass = request.POST.get('PassWord')
    if(vol_pass=='vol123'):
        return render(request, 'umdsite/VolunteerProfile.html')

    return render(request, 'umdsite/VolunteerLogin.html')

def VolunteerProfile(request):
    return render(request, 'umdsite/VolunteerProfile.html')

def certificate(request):
    return render(request, 'umdsite/certificate.html')
