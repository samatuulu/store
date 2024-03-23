from django.urls import path
from .views import UserSignUpAPIView, UserLoginAPIView


urlpatterns = [
    path('signup/', UserSignUpAPIView.as_view(), name='signup_url'),
    path('login/', UserLoginAPIView.as_view(), name='login_url'),
]
