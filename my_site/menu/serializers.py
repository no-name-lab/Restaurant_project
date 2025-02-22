from rest_framework import serializers
from .models import *


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'restaurant_name', 'text', 'location', 'hotline']


class AboutUsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsImage
        fields = ['id', 'about_us', 'images']


class AboutUsSerializer(serializers.ModelSerializer):
    about_us = AboutUsImageSerializer(read_only=True, many=True)
    class Meta:
        model = AboutUs
        fields = ['id', 'title', 'about_us', 'description_about', 'address', 'working_days', 'opening_time', 'closing_time']


class BestSellerPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestsellerPhotos
        fields = ['id', 'bestseller', 'photos']


class BestSellersSerializer(serializers.ModelSerializer):
    photo = BestSellerPhotosSerializer(read_only=True, many=True)
    class Meta:
        model = BestSellers
        fields = ['id', 'best_name', 'description', 'photo']


class ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extra
        fields = ['id', 'extra_name', 'extra_price', 'product']


class DrinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        fields = ['id', 'drink_name', 'drink_price', 'product']


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'product_description', 'price']


class ProductDetailSerializer(serializers.ModelSerializer):
    drinks = DrinksSerializer(read_only=True, many=True)
    extra = ExtraSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'product_image', 'product_description', 'price', 'drinks', 'extra']


class CategoryListSerializer(serializers.ModelSerializer):
    foods = ProductListSerializer(read_only=True, many=True)
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'foods']


class CategoryDetailSerializer(serializers.ModelSerializer):
    foods = ProductDetailSerializer(read_only=True, many=True)
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'foods']


class MenuListSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer()
    class Meta:
        model = Menu
        fields = ['id', 'category', 'menu_name', 'menu_description']


class MenuDetailSerializer(serializers.ModelSerializer):
    category = CategoryDetailSerializer()
    class Meta:
        model = Menu
        fields = ['id', 'category', 'menu_name', 'menu_description']


class InteriorImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteriorImages
        fields = ['id', 'interior_images']


class InteriorSerializer(serializers.ModelSerializer):
    interior_images = InteriorImagesSerializer(read_only=True, many=True)
    class Meta:
        model = Interior
        fields = ['id', 'interior_title', 'interior_images',]


class SocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = ['id', 'network_name', 'network_url']


class ContactInfoSerializer(serializers.ModelSerializer):
    contact = SocialNetworkSerializer(read_only=True, many=True)
    class Meta:
        model = ContactInfo
        fields = ['id', 'contact_number', 'email', 'contact_address', 'contact']
