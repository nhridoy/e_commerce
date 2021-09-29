from django.shortcuts import render
from productapp.models import Product, ProductImages, Coupon, Sizes, Colors, Rating
from productapp.forms import RatingForm
from django.http import HttpResponseRedirect


# Create your views here.

def productDetailsView(request, product_slug):
    product = Product.objects.get(product_slug=product_slug)
    user_ratings = Rating.objects.filter(user=request.user).values_list('product', flat=True)
    if request.method == 'POST':
        star = int(request.POST.get('rating'))
        comment = request.POST.get('review')
        rate = Rating(user=request.user, product_rating=star, product_comment=comment, product=product)
        rate.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
        # return HttpResponseRedirect(request.path_info)
    context = {
        'product': product,
        'user_ratings': user_ratings,
    }
    return render(request, 'home/product-details.html', context)


def wishlistView(request):
    context = {

    }
    return render(request, 'home/wishlist.html', context)


def cartView(request):
    context = {

    }
    return render(request, 'home/cart.html', context)
