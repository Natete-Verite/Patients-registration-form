from django.shortcuts import render
from .forms import PatientRegistrationForm
from .models import Patient
# Create your views here.

def register_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PatientRegistrationForm()
    return render(request,"recordspatients/register_patient.html",{'form':form}) 

def list_patients(request):
    patients = Patient.objects.all()   
    return render(request, "recordspatients/list_patient.html", {"patients":patients})        