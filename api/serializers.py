from rest_framework import serializers
from .models import User,Doctor,Specialization,Booking

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model=User

        fields=['id','username','email','password','first_name','last_name','is_superuser']

        read_only_fields=['id','is_superuser']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class DoctorSerializer(serializers.ModelSerializer):

    specialization=serializers.StringRelatedField()

    class Meta:

        model=Doctor

        fields="__all__"

        read_only_fields=['id']


class SpecializationSerialiser(serializers.ModelSerializer):

    doctor=DoctorSerializer(read_only=True,many=True)

    class Meta:

        model=Specialization

        fields="__all__"

        read_only_fields=['id']


class BookingSerializer(serializers.ModelSerializer):

    doctor=serializers.StringRelatedField(read_only=True)

    user=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Booking

        fields="__all__"

        read_only_fields=['id','created_date','is_active','booking_no']