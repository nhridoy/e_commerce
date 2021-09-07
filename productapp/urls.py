from django.urls import path
from productapp import views

app_name = 'product_details_app'

urlpatterns = [
    path('', views.productDetailsView, name='product'),
    path('all/', views.allProductsView, name='product-list'),
    path('wishlist/', views.wishlistView, name='wish-list'),
    path('cart/', views.cartView, name='cart'),
]