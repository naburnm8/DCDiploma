from django.urls import path
from products import views

app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
]
