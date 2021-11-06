from django.urls import path
from productapp import views

app_name = 'product_details_app'

urlpatterns = [
    path('<product_slug>/', views.productDetailsView, name='product'),
    path('add_to_wishlist/<product_slug>/', views.addToWishListView, name='add_to_wishlist'),
    path('remove_from_wishlist/<id>/', views.removeFromWishListView, name='remove_from_wishlist'),

]
