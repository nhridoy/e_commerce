from django.shortcuts import render
from apiapp import serializers
from productapp import models
from rest_framework import generics


# Create your views here.

class ProductApiView(generics.RetrieveAPIView):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    lookup_field = 'product_slug'

    # def get_queryset(self):
    #     field = self.kwargs.get('product_slug')
    #     return models.Product.objects.get(product_slug=field)
