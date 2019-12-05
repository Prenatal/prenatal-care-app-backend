from django.urls import path


from .api import (
    UserRegistrationAPIView,
)

urlpatterns = [
    path('users/', UserRegistrationAPIView.as_view()),
]
