

from django.urls import path
from .views import (DoctorApiView,DoctorDetailApiView,PatientApiView,ReactApiView,
                    PatientDetailApiView,AppointmentApiView,AppointmentDetailApiView)

urlpatterns = [
    
    path('', DoctorApiView.as_view(), name='doctor-list'),
    path('doctor/<int:pk>/', DoctorDetailApiView.as_view(), name='doctor-detail'),
    
    path('patients/', PatientApiView.as_view(), name='patient-list'),
    path('patients/<int:pk>/', PatientDetailApiView.as_view(), name='patient-detail'),
    
    path('appointments/', AppointmentApiView.as_view(), name='appointment-list'),
    path('appointments/<int:pk>/', AppointmentDetailApiView.as_view(), name='appointment-detail'),
    
    path('react/', ReactApiView.as_view(), name='react-list'),
    
]


