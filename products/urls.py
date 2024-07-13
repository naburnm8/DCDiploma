from django.urls import path
from products import views

app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.category, name='category'),
]
