from django.shortcuts import render
from products.models import Product, Category


def index(request):
    context = {
        'products': Product.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'products/index.html', context)


def category(request, category_id=None):
    products = Product.objects.filter(category=category_id) if category_id else Product.objects.all()
    context = {
        'products': products,
        'categories': Category.objects.all()
    }
    return render(request, 'products/index.html', context)
