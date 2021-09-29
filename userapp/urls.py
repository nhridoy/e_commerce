from django.urls import path
from userapp import views
app_name = 'profile_app'

urlpatterns = [
    path('', views.profileView, name='profile'),
    path('orders/', views.historyView, name='order-history'),
    path('logout/', views.logoutView, name='logout'),
    path('login/', views.loginView, name='login'),
    path('signup/', views.registrationView, name='signup'),
    path('edit-info/', views.editProfileView, name='edit-profile'),
    path('change-password/', views.changePasswordView, name='change-password'),
    path('edit-billing-address/', views.editBillingAddressView, name='edit-billing-address'),
    path('edit-shipping-address/', views.editShippingAddressView, name='edit-shipping-address'),
]