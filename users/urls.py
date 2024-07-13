from users.views import UserRegistrationView, UserLoginView, logout_view, UserProfileView
from django.urls import path

app_name = 'users'
urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
]
