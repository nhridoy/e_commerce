from django.shortcuts import render, get_object_or_404
from productapp.models import Product, ProductImages, Coupon, Sizes, Colors, Rating, WishList
from productapp.forms import RatingForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.

def productDetailsView(request, product_slug):
    product = Product.objects.get(product_slug=product_slug)
    try:
        user_ratings = Rating.objects.filter(user=request.user).values_list('product', flat=True)
    except:
        pass
    if request.method == 'POST':
        star = int(request.POST.get('rating'))
        comment = request.POST.get('review')
        rate = Rating(user=request.user, product_rating=star, product_comment=comment, product=product)
        rate.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
        # return HttpResponseRedirect(request.path_info)
    try:
        context = {
            'product': product,
            'user_ratings': user_ratings,
        }
    except:
        context = {
            'product': product,
        }
    return render(request, 'home/product-details.html', context)


@login_required
def addToWishListView(request, product_slug):
    current_product = Product.objects.get(product_slug=product_slug)
    addToWishList = WishList.objects.create(user=request.user, product=current_product)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def removeFromWishListView(request, id):
    current_wishlist = WishList.objects.get(id=id, user=request.user)
    current_wishlist.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])



