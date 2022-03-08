from rest_framework import serializers
from productapp import models


class ProductSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company_name.company_name')
    total_rating_count = serializers.IntegerField()
    avg_rating = serializers.IntegerField()
    class Meta:
        model = models.Product
        fields = '__all__'
