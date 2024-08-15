from django.contrib import admin
from .models import User,Booking,Doctor,Specialization


admin.site.register(Doctor)
admin.site.register(Specialization)
admin.site.register(Booking)