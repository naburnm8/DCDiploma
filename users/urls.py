from users.views import UserRegistrationView, UserLoginView, logout_view
from django.urls import path

app_name = 'users'
urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout')
]
