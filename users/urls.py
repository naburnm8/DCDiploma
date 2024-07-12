from users.views import UserRegistrationView, UserLoginView
from django.urls import path

app_name = 'users'
urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
]
