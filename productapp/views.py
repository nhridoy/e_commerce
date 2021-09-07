from django.shortcuts import render
from productapp.models import Product, ProductImages, Coupon, Sizes, Colors

# Create your views here.

def productDetailsView(request):
    context = {

    }
    return render(request, 'home/product-details.html', context)

def allProductsView(request):
    context = {

    }
    return render(request, 'home/all-products.html', context)


def wishlistView(request):
    context = {

    }
    return render(request, 'home/wishlist.html', context)

def cartView(request):
    context = {

    }
    return render(request, 'home/cart.html', context)