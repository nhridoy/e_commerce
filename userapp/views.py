from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from userapp.forms import LoginForm, RegistrationForm, EditProfileForm, EditShippingAddressForm, EditBillingAddressForm
from productapp.models import WishList
from purchaseapp.models import Cart, Order


# Create your views here.
def login_executed(redirect_to):
    """This Decorator kicks authenticated user out of a view"""

    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to)
            return view_method(request, *args, **kwargs)

        return _arguments_wrapper

    return _method_wrapper


@login_required
def profileView(request):
    context = {

    }
    return render(request, 'home/profile.html', context)


@login_required
def historyView(request):
    context = {

    }
    return render(request, 'home/order-history.html', context)


@login_required
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('ecom_app:index'))


@login_executed('ecom_app:index')
def loginView(request):
    form = LoginForm()
    next_page = request.GET.get('next')
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        username, password = request.POST.get('username'), request.POST.get('password')
        if user := authenticate(username=username, password=password):
            if user.is_active:
                login(request, user)
                if next_page:
                    return redirect(next_page)
                return HttpResponseRedirect(reverse('ecom_app:index'))

    context = {
        'form': form,
    }

    return render(request, 'home/login.html', context)


@login_executed('ecom_app:index')
def registrationView(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('ecom_app:index'))
    context = {
        'form': form,
    }

    return render(request, 'home/registration.html', context)


@login_required
def editProfileView(request):
    form = EditProfileForm(instance=request.user.user_profile)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile_app:profile'))

    context = {
        'form': form,
    }
    return render(request, 'home/edit-info.html', context)


@login_required
def editBillingAddressView(request):
    form = EditBillingAddressForm(instance=request.user.user_billing_address)
    if request.method == 'POST':
        form = EditBillingAddressForm(request.POST, instance=request.user.user_billing_address)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile_app:profile'))

    context = {
        'form': form,
    }
    return render(request, 'home/edit-info.html', context)


@login_required
def editShippingAddressView(request):
    form = EditShippingAddressForm(instance=request.user.user_shipping_address)
    if request.method == 'POST':
        form = EditShippingAddressForm(request.POST, instance=request.user.user_shipping_address)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile_app:profile'))

    context = {
        'form': form,
    }
    return render(request, 'home/edit-info.html', context)


@login_required
def changePasswordView(request):
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile_app:profile'))

    context = {
        'form': form,
    }
    return render(request, 'home/edit-info.html', context)


@login_required
def wishlistView(request):
    wishlists = WishList.objects.filter(user=request.user)
    context = {
        'wishlists': wishlists
    }
    return render(request, 'home/wishlist.html', context)


@login_required
def cartView(request):
    carts = Cart.objects.filter(user=request.user)
    order = Order.objects.get(user=request.user, is_ordered=False)
    context = {
        'carts': carts,
        'order': order,
    }
    return render(request, 'home/cart.html', context)
