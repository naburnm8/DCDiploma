from django.urls import path, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('', include('products.urls', namespace='products')),
    path('order/', include('cart.urls', namespace='cart')),
]
