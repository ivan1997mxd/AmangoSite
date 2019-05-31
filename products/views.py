from django.shortcuts import render
from .models import Product


def product_list(request):
    context = {'products': Product.objects.all()}
    return render(request, 'products.html', context)

