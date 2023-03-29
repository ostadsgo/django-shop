from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request,"store/home.html", {"products": products})

def product_info(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, "store/product-info.html", {"product": product})