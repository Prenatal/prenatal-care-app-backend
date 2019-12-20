from django.urls import path


from .api import (
    UserRegistrationAPIView,
    UserLoginAPIView,
    
)

urlpatterns = [
    path('users/signup/', UserRegistrationAPIView.as_view()),
    path('users/login/', UserLoginAPIView.as_view()),
]