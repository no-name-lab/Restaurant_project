from django.urls import path, include
from .views import *
urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),

    path('product/', ProductListAPIView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),

    path('menu/', MenuListAPIView.as_view(), name='menu_list'),
    path('menu/<int:pk>/', MenuDetailAPIView.as_view(), name='menu_detail'),

    path('restaurant/', RestaurantViewSet.as_view(), name='restaurant_list'),
    path('about_us/', AboutUsViewSet.as_view(), name='about_list'),
    path('bestsellers/', BestSellersViewSet.as_view(), name='bestsellers_list'),
    path('interior/', InteriorViewSet.as_view(), name='interior_list'),
    path('contact/', ContactInfoViewSet.as_view(), name='contact_list'),
    path('social/', SocialNetworkViewSet.as_view(), name='social_list'),

]