from django.contrib import admin
from myapp.models import User, Products, Appointments, contact, Member

# Register your models here.
admin.site.register(User)
admin.site.register(Products)
admin.site.register(Appointments)
admin.site.register(contact)
admin.site.register(Member)