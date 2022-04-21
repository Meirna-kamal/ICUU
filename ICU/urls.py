from django.urls import path,include
from . import views

urlpatterns = [
    path('PostVitalSigns/', views.PostvitalSigns.as_view(), name='postvitalsigns'),
    path('GetVitalSigns/', views.GetvitalSigns.as_view(), name='getvitalsigns')
]