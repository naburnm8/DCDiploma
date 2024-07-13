from django.http import HttpResponseRedirect
from django.shortcuts import render
from products.models import Product, Category, Basket



def index(request):
    context = {
        'title': 'SKUFF DELIVERY',
        'products': Product.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'products/index.html', context)


def category(request, category_id=None):
    products = Product.objects.filter(category=category_id) if category_id else Product.objects.all()
    context = {
        'title': 'SKUFF DELIVERY',
        'products': products,
        'categories': Category.objects.all()
    }
    return render(request, 'products/index.html', context)


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_view(request):
    context = {
        'baskets': Basket.objects.filter(user=request.user)
    }
    return render(request, 'products/basket.html', context)


def basket_remove(request, id):
    basket = Basket.objects.get(pk=id)
    if basket.quantity == 1:
        basket.delete()
    else:
        basket.quantity -= 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])



