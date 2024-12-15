from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment, User

@login_required
def dashboard(request):
    if request.user.role == 'patient':
        appointments = Appointment.objects.filter(patient=request.user)
        return render(request, 'hospital/patient_dashboard.html', {'appointments': appointments})
    elif request.user.role == 'doctor':
        appointments = Appointment.objects.filter(doctor=request.user)
        return render(request, 'hospital/doctor_dashboard.html', {'appointments': appointments})
    elif request.user.role == 'admin':
        return render(request, 'hospital/admin_dashboard.html')
    else:
        return redirect('/')

@login_required
def book_appointment(request):
    if request.method == 'POST':
        # Placeholder for booking logic
        return redirect('dashboard')
    return render(request, 'hospital/book_appointment.html')
