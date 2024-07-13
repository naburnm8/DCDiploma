from django.urls import path
from products import views
from products.views import basket_add, basket_view, basket_remove

app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/view/', basket_view, name='basket_view'),
    path('baskets/remove/<int:id>/', basket_remove, name='basket_remove'),
]
