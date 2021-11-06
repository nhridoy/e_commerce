from django.urls import path
from purchaseapp import views

app_name = 'purchase_app'

urlpatterns = [
    path('add/<product_slug>', views.addToCartView, name='add_to_cart'),
    path('plus/<product_slug>', views.addToCartView, name='plus_to_cart'),
    path('minus/<product_slug>', views.addToCartView, name='minus_to_cart'),
    path('remove/<product_slug>', views.addToCartView, name='remove_from_cart'),
]