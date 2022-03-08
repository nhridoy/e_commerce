from django.urls import path
from apiapp import views
app_name = 'api_app'
urlpatterns = [
    path('product/<product_slug>/', views.ProductApiView.as_view(), name='product'),
]