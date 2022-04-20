from django.contrib import admin
from .models import user_registration,volunteer_login,donated_medicine,requested_medicine,user_query,user_login

# Register your models here.
admin.site.register(user_registration)
admin.site.register(volunteer_login)
admin.site.register(donated_medicine)
admin.site.register(requested_medicine)
admin.site.register(user_query)
admin.site.register(user_login)