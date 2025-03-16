
from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mentors/', MentorListAPIView.as_view() ),
    path('mentors/<int:pk>/', MentorRetrieveUpdateDeleteAPIView.as_view() ),
    path('guruh/', GuruhListAPIView.as_view() ),
    path('student/', StudentListAPIView.as_view() ),
    path('backend-guruh/', BackendGuruhListAPIView.as_view() ),
    path('guruh/<int:pk>/', GuruhRetrieveUpdateDeleteAPIView.as_view() ),
    path('student/<int:pk>/', StudentRetrieveUpdateDeleteAPIView.as_view() ),
]
