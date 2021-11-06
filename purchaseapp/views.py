from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from purchaseapp.models import Cart, Product, User, Order


# Create your views here.
@login_required
def addToCartView(request, product_slug):
    current_product = get_object_or_404(Product, product_slug=product_slug)
    new_cart = Cart.objects.get_or_create(user=request.user, product=current_product, is_purchased=False)
    current_order = Order.objects.get_or_create(user=request.user, is_ordered=False)

    if current_order[1]:
        current_order[0].cart.add(new_cart[0])
        current_order[0].save()
    else:
        if not current_order[0].cart.filter(product=current_product).exists():
            current_order[0].cart.add(new_cart[0])
            current_order[0].save()
        else:
            new_cart[0].quantity += 1
            new_cart[0].save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def increaseCartView(request, product_slug):
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def decreaseCartView(request, product_slug):
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def deleteCartView(request, product_slug):
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
