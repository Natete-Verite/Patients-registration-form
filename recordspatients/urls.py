from django.urls import path
from .views import filter_age_patients, list_patients, register_patient

urlpatterns = [
    path('register/', register_patient, name="patient"),    
    path('patients/', list_patients, name="patients"),
    path('filtered/', filter_age_patients, name="filtered"),
]
