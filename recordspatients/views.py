from django.shortcuts import render,redirect
from .forms import PatientRegistrationForm
from .models import Patient
# Create your views here.

def register_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patients')
    else:
        form = PatientRegistrationForm()
    return render(request, "register_patient.html", {'form': form})

def list_patients(request):
    patients = Patient.objects.all()   
    return render(request, 'list_patients.html', {'patients':patients})        

def filter_age_patients(request):
    patients = Patient.objects.filter(age__lte= 18)   
    return render(request, 'list_patients.html', {'patients':patients})