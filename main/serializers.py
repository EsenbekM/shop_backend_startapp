from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCreateValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=1, max_length=200)
    description = serializers.CharField()
    price = serializers.IntegerField()
    brand = serializers.IntegerField()
    size = serializers.ListField()

    def validate_category(self, brand):
        try:
            Product.objects.get(id=brand)
        except Product.DoesNotExist:
            raise ValidationError("This category doesn't exist!")

    def validate_title(self, name):
        if Product.objects.filter(name=name):
            raise ValidationError("This Product already exist!")