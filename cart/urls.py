from django.urls import path
from .views import OrderView, SuccessTemplateView, CancelTemplateView

app_name = 'cart'
urlpatterns = [
    path('', OrderView.as_view(), name='order_view'),
    path('success/', SuccessTemplateView.as_view(), name='success_order'),
    path('canсel/', CancelTemplateView.as_view(), name='cancel_order'),
]
