from django.urls import path
from .views import LoginAPI, RegisterAPI, item_list, studentData 

urlpatterns = [
    path('items/', item_list, name='item-list'),
    path('students/', studentData, name='student-data'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
]