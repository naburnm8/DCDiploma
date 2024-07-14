from django.urls import path
from .views import OrderView, SuccessTemplateView, CanselTemplateView

app_name = 'cart'
urlpatterns = [
    path('', OrderView.as_view(), name='order_view'),
    path('success/', SuccessTemplateView.as_view(), name='success_order'),
    path('cansel/', CanselTemplateView.as_view(), name='cansel_order'),
]
