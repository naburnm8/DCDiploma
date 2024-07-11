from users.views import UserRegistrationView
from django.urls import path

app_name = 'users'
urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='registration'),
]