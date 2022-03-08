from rest_framework import serializers
from productapp import models

class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Colors
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company_name.company_name')
    product_colors = ProductColorSerializer(many=True)
    product_sizes = serializers.StringRelatedField(many=True)
    total_rating_count = serializers.IntegerField()
    avg_rating = serializers.IntegerField()
    class Meta:
        model = models.Product
        fields = '__all__'
