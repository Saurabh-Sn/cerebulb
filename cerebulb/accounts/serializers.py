from rest_framework import serializers
from django.http import Http404
from .models import  Category, Product


class categorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['category_name', 'category_code']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id','product_name', 'product_code', 'product_images', 'product_mfg_date', 'product_category']
        extra_kwargs = {
            'id': {'read_only': True}
        }


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        max_length=100,
        label='',
        style={'placeholder': 'Email', 'autofocus': True}
    )
    password = serializers.CharField(
        max_length=100,
        label='',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    remember_me = serializers.BooleanField(label='Remember Me')


class ListCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [ 'id', 'category_name', 'category_code']


class ListProductSerializer(serializers.ModelSerializer):
    product_category = serializers.SerializerMethodField()


    class Meta:
        model = Product
        fields = ['id','product_name', 'product_code', 'product_images', 'product_mfg_date', 'product_category']
        extra_kwargs = {
            'id': {'read_only': True}
        }

    def get_product_category(self, obj):
        return obj.product_category.category_name
