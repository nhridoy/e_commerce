from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse
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
    elif current_order[0].cart.filter(product=current_product).exists():
        new_cart[0].quantity += 1
        new_cart[0].save()

    else:
        current_order[0].cart.add(new_cart[0])
        current_order[0].save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def increaseCartView(request, product_slug):
    current_product = Product.objects.get(product_slug=product_slug)
    try:
        current_cart = Cart.objects.get(user=request.user, product=current_product, is_purchased=False)
        current_cart.quantity += 1
        current_cart.save()
    except:
        return HttpResponse('404')

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def decreaseCartView(request, product_slug):
    current_product = Product.objects.get(product_slug=product_slug)
    try:
        current_cart = Cart.objects.get(user=request.user, product=current_product, is_purchased=False)
        if current_cart.quantity <= 1:
            current_cart.delete()
        else:
            current_cart.quantity -= 1
            current_cart.save()
    except:
        return HttpResponse('404')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def deleteCartView(request, cart_id):
    current_cart = Cart.objects.get(id=cart_id)
    current_cart.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
