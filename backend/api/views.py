from django.shortcuts import render
from api.models import Patient,Doctor,Appointment,React
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from api.serializers import PatientSerializer,DoctorSerializer,AppointmentSerializer,ReactSerializer


#Doctor serializer Views

class DoctorApiView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    
    # print("Patient",queryset)

    def list(self, request):
        try:
            queryset = Doctor.objects.all()
            serializer = DoctorSerializer(queryset, many=True)
            return Response(serializer.data)
        except Doctor.DoesNotExist:
            raise NotFound(detail="Doctor not found", code=404)
    

    
    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DoctorDetailApiView(APIView):
    
    def get(self, request, pk):
        try:
            doctor = Doctor.objects.get(id=pk)
        except Doctor.DoesNotExist:
            raise NotFound(detail="Doctor not found", code=404)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)
    
    def put(self, request,pk):
        doctor = Doctor.objects.get(id=pk)
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk):
        doctor = Doctor.objects.get(id=pk)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    


# Patient serializer views
class PatientApiView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
    # print("Patient",queryset)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = PatientSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PatientDetailApiView(APIView):
    
    def get(self, request, pk):
        try:
            patient = Patient.objects.get(id=pk)
        except Patient.DoesNotExist:
            raise NotFound(detail="Patient not found", code=404)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    
    def put(self, request,pk):
        patient = Patient.objects.get(id=pk)
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk):
        patient = Patient.objects.get(id=pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

# Appointment Serializer views
class AppointmentApiView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    
    # print("Appointment",queryset)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = AppointmentSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class AppointmentDetailApiView(APIView):
    
    def get(self, request, pk):
        try:
            appointment = Appointment.objects.get(id=pk)
        except Appointment.DoesNotExist:
            raise NotFound(detail="Appintment not found", code=404)
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)
    
    
    def put(self, request,pk):
        appointment = Appointment.objects.get(id=pk)
        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk):
        appointment = Appointment.objects.get(id=pk)
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    



class ReactApiView(APIView):
    serializers_classes=ReactSerializer
    
    def get(self,request):
        detail=[{"name":detail.name,"detail":detail.detail}
        for detail in React.objects.all()]
        return Response(detail)
        
    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)