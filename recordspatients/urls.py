from django.urls import path
from .views import list_patients, register_patient

urlpatterns = [
    path('register/', register_patient, name="patient"),    
    path('patients/', list_patients, name="patients"),
]
