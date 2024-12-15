from django.contrib import admin
from .models import User, PatientProfile, DoctorProfile, Appointment, Billing

admin.site.register(User)
admin.site.register(PatientProfile)
admin.site.register(DoctorProfile)
admin.site.register(Appointment)
admin.site.register(Billing)

# Step 7: Add Views in hospital/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment, Billing

@login_required
def dashboard(request):
    if request.user.role == 'patient':
        return render(request, 'hospital/patient_dashboard.html')
    elif request.user.role == 'doctor':
        return render(request, 'hospital/doctor_dashboard.html')
    else:
        return render(request, 'hospital/admin_dashboard.html')

@login_required
def book_appointment(request):
    if request.method == 'POST':
        # Logic to handle appointment booking
        pass
    return render(request, 'hospital/book_appointment.html')
