from rest_framework import viewsets, generics
from rest_framework.response import Response

from .serializers import *
from .models import *


class RestaurantViewSet(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class AboutUsViewSet(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class AboutUsImageViewSet(generics.ListAPIView):
    queryset = AboutUsImage.objects.all()
    serializer_class = AboutUsImageSerializer


class BestSellersViewSet(generics.ListAPIView):
    queryset = BestSellers.objects.all()
    serializer_class = BestSellersSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDetailAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class MenuListAPIView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuListSerializer


class MenuDetailAPIView(generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuDetailSerializer


class InteriorViewSet(generics.ListAPIView):
    queryset = Interior.objects.all()
    serializer_class = InteriorSerializer


class ContactInfoViewSet(generics.ListAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer


class SocialNetworkViewSet(generics.ListAPIView):
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialNetworkSerializer


