from rest_framework import serializers
from productapp import models


class ProductSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField()
    class Meta:
        model = models.Product
        fields = '__all__'
