from django.shortcuts import render

# Create your views here.
# in fisierul marketplaceapp\views.py

from django.http import HttpResponse
from .models import Product


def index(request):
    return render(request, "marketplaceapp/home.html")


def product_list(request):
    all_products = Product.objects.all()
    context = {
        "products": all_products
    }
    return render(request, "marketplaceapp/product_list.html", context)


def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    context = {
        "product": product
    }
    return render(request, "marketplaceapp/product_detail.html", context)
