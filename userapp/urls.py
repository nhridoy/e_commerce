from django.urls import path
from userapp import views
app_name = 'profile_app'

urlpatterns = [
    path('', views.profileView, name='profile'),
    path('orders/', views.historyView, name='order-history'),
]