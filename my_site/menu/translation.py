from .models import Product, Category, BestSellers, AboutUs, Restaurant, Menu, Interior, Extra, Drinks
from modeltranslation.translator import TranslationOptions,register

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'product_description')


@register(Extra)
class ExtraTranslationOptions(TranslationOptions):
    fields = ('extra_name', )


@register(Drinks)
class DrinkTranslationOptions(TranslationOptions):
    fields = ('drink_name',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name', )


@register(BestSellers)
class BestSellerTranslationOptions(TranslationOptions):
    fields = ('best_name', 'description')


@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('title', 'description_about')


@register(Restaurant)
class RestaurantTranslationOptions(TranslationOptions):
    fields = ('restaurant_name', 'text')


@register(Menu)
class MenuTranslationOptions(TranslationOptions):
    fields = ('menu_name', 'menu_description')


@register(Interior)
class InteriorTranslationOptions(TranslationOptions):
    fields = ('interior_title',)


