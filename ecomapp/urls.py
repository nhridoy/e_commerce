from django.urls import path
from ecomapp import views

app_name = 'ecom_app'

urlpatterns = [
    path('', views.indexView, name='index'),
    path('all/<category>', views.pageView, name='all'),
    path('filter/', views.filterView, name='filter'),
]