from django.shortcuts import render
from rest_framework.response import Response
from .serializers import UserSerializer,DoctorSerializer,SpecializationSerialiser,BookingSerializer
from rest_framework.generics import CreateAPIView,UpdateAPIView,RetrieveDestroyAPIView,ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User,Booking,Doctor,Specialization
from rest_framework import permissions,authentication,status
from .permissions import isAdminOrReadOnly,isOwnerorAdmin
from datetime import datetime


class UserRegister(CreateAPIView):

    serializer_class=UserSerializer

    queryset=User.objects.all()

class AdminLogin(APIView):

    permission_classes=[permissions.IsAuthenticated]

    authentication_classes=[JWTAuthentication]

    def get(self, request, *args, **kwargs):

        qs=User.objects.get(username=request.user)

        serializer=UserSerializer(qs)

        return Response(serializer.data,status=status.HTTP_200_OK)

class DoctorCreateView(APIView):
    
    permission_classes=[permissions.IsAdminUser]

    authentication_classes=[JWTAuthentication]

    def post(self, request, *args, **kwargs):
        
        sp=Specialization.objects.get(id=kwargs.get('pk'))
        
        serializer=DoctorSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(specialization=sp)

            return Response(serializer.data,status=status.HTTP_200_OK)
        else:

            return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        
class DoctorList(ListAPIView):

    permission_classes=[permissions.IsAuthenticated]

    authentication_classes=[JWTAuthentication]

    queryset=Doctor.objects.all()

    serializer_class=DoctorSerializer

class DoctorRetrieveDeleteView(RetrieveDestroyAPIView):

    serializer_class=DoctorSerializer

    queryset=Doctor.objects.all()

    permission_classes=[isAdminOrReadOnly]

    authentication_classes=[JWTAuthentication]

class DoctorUpdateView(UpdateAPIView):

    def put(self,request,*args,**kwargs):

        specialization=Specialization.objects.get(id=kwargs.get('sp'))

        qs=Doctor.objects.get(id=kwargs.get('pk'))

        serializer=DoctorSerializer(instance=qs,data=request.data)

        if serializer.is_valid():

            serializer.save(specialization=specialization)

            return Response(serializer.data,status=status.HTTP_200_OK)
        
        else:

            return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

class SpecialisationModelViewSet(ModelViewSet):
    
    serializer_class=SpecializationSerialiser

    queryset=Specialization.objects.all()

    permission_classes=[isAdminOrReadOnly]

    authentication_classes=[JWTAuthentication]

class BookingCreateView(APIView):

    permission_classes=[permissions.IsAuthenticated]

    authentication_classes=[JWTAuthentication]

    def post(self, request, *args, **kwargs):

        doc=Doctor.objects.get(id=kwargs.get('pk'))

        serializer=BookingSerializer(data=request.data)

        if serializer.is_valid():

            b_date=serializer.validated_data.get('booking_date')

            count=Booking.objects.filter(booking_date=b_date).count()

            serializer.save(doctor=doc,user=request.user,booking_no=count+1,booking_date=b_date)

            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

class Bookinglist(APIView):

    permission_classes=[permissions.IsAuthenticated]

    authentication_classes=[JWTAuthentication]

    def get(self, request, *args, **kwargs):

        qs=Booking.objects.filter(user=request.user).order_by("-id")

        serializer=BookingSerializer(qs,many=True)

        return Response(serializer.data)
        
class BookingReatriveDelete(RetrieveDestroyAPIView):

    permission_classes=[isOwnerorAdmin]

    authentication_classes=[JWTAuthentication]

    serializer_class=BookingSerializer

    queryset=Booking.objects.all()

    def perform_destroy(self, instance):
        
        instance.is_active=False

        instance.save()

class BookingViewAdmin(APIView):

    permission_classes=[permissions.IsAdminUser]

    authentication_classes=[JWTAuthentication]

    def get(self, request, *args, **kwargs):

        qs=Booking.objects.all()


        if "date" in request.query_params:

            date=request.query_params.get('date')

            qs=qs.filter(booking_date=date)
        
        if "doctor" in request.query_params:

            doctorid=request.query_params.get('doctor')

            doctor=Doctor.objects.get(id=doctorid)

            qs=qs.filter(doctor=doctor)
        
        serialiser=BookingSerializer(qs,many=True)

        return Response(serialiser.data,status=status.HTTP_200_OK)