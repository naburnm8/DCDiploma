from datetime import datetime
from http import HTTPStatus

import stripe
from django.http import HttpResponseRedirect, HttpResponse

from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.conf import settings

from cart.forms import OrderForm
from cart.models import Cart
from products.models import Basket, BasketQuerySet

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessTemplateView(TemplateView):
    template_name = 'cart/success.html'


class CanselTemplateView(TemplateView):
    template_name = 'cart/cansel.html'


class OrderView(CreateView):
    template_name = 'cart/order-create.html'
    success_url = reverse_lazy('cart:order_view')
    form_class = OrderForm

    def post(self, request, *args, **kwargs):
        super(OrderView, self).post(request, *args, **kwargs)
        baskets = Basket.objects.filter(user=self.request.user)
        line_items = []
        for basket in baskets:
            item = {
                'price': basket.product.stripe_product_price_id,
                'quantity': basket.quantity,
            }
            line_items.append(item)

        checkout_session = stripe.checkout.Session.create(
            line_items=line_items,
            mode='payment',
            success_url='{}{}'.format(settings.DOMAIN_NAME, reverse('cart:success_order')),
            cancel_url='{}{}'.format(settings.DOMAIN_NAME, reverse('cart:cansel_order')),
        )
        return HttpResponseRedirect(checkout_session.url, status=HTTPStatus.SEE_OTHER)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(OrderView, self).form_valid(form)
