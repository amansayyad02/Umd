from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="sitehome"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("login/",views.login,name="login"),
    path("register/",views.register,name="register"),
    path("donation/",views.donation,name="donation"),
    path("request/",views.request,name="request"),
    path("UserProfile/",views.UserProfile,name="UserProfile"),
    path("VolunteerLogin/",views.VolunteerLogin,name="VolunteerLogin"),
    path("VolunteerProfile/",views.VolunteerProfile,name="VolunteerProfile"),
    path("certificate/",views.certificate,name="certificate"),
]