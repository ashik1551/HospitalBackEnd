from django.urls import path
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('specialization',views.SpecialisationModelViewSet,basename='specialization')


urlpatterns=[
    path('user/',views.UserRegister.as_view()),
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),
    path('specialization/<int:pk>/doctor/',views.DoctorCreateView.as_view()),
    path('doctor/<int:pk>/',views.DoctorRetrieveDeleteView.as_view()),
    path('<int:sp>/doctor/<int:pk>/',views.DoctorUpdateView.as_view()),
    path('doctor/<int:pk>/booking/',views.BookingCreateView.as_view()),
    path('booking/<int:pk>/',views.BookingReatriveDelete.as_view()),
    path('booking/',views.Bookinglist.as_view()),
    path('booking/admin/',views.BookingViewAdmin.as_view()),
    path('isadmin/',views.AdminLogin.as_view()),
    path('doctor/',views.DoctorList.as_view())
] + router.urls