from django.urls import path
from productapp import views

app_name = 'product_details_app'

urlpatterns = [
    path('<product_slug>/', views.productDetailsView, name='product'),
    path('wishlist/', views.wishlistView, name='wish-list'),
    path('cart/', views.cartView, name='cart'),
]