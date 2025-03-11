from rest_framework import serializers
from .models import Patient,Doctor,Appointment,React


# 1.DoctorSerializer: This serializer will represent the Doctor model and will include related Patient objects
# by using the related_name="patients" for the ForeignKey relationship.

#2.PatientSerializer: This serializer will represent the Patient model and include the related Doctor objects
# by using the related_name="appointments" for the ForeignKey relationship.

#3.AppointmentSerializer: This serializer will represent the Appointment model and will include related Doctor
# and Patient fields, leveraging StringRelatedField or other appropriate fields for these relations.



class DoctorSerializer(serializers.ModelSerializer):
    # Nested PatientSerializer to show all patients associated with the doctor
    patients = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    doctor = serializers.CharField(read_only=True)
    appointments = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Patient
        fields = '__all__'
        # exclude =('doctor', ) 


class AppointmentSerializer(serializers.ModelSerializer):
    doctor= serializers.StringRelatedField(read_only=True)
    patient = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Appointment
        fields = '__all__'
        # exclude = ('doctor',)



class ReactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=React
        fields="__all__"
    