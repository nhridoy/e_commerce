from django.urls import path
from ecomapp import views

app_name = 'ecom_app'

urlpatterns = [
    path('', views.indexview, name='index'),
]