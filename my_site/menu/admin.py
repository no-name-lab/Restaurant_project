from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin


class ExtraInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = Extra
    extra = 1


class DrinksInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = Drinks
    extra = 1


class BestSellerPhotosInline(admin.TabularInline):
    model = BestsellerPhotos
    extra = 1


class AboutUsImageInline(admin.TabularInline):
    model = AboutUsImage
    extra = 1


class SocialNetworkInline(admin.TabularInline):
    model = SocialNetwork
    extra = 1


class InteriorImagesInline(admin.TabularInline):
    model = InteriorImages
    extra = 1


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    inlines = [ExtraInline, DrinksInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(AboutUs)
class AboutUsAdmin(TranslationAdmin):
    inlines = [AboutUsImageInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(BestSellers)
class BestSellersAdmin(TranslationAdmin):
    inlines = [BestSellerPhotosInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Interior)
class InteriorAdmin(TranslationAdmin):
    inlines = [InteriorImagesInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Restaurant, Menu, Category)
class RestaurantAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class ContactInfoAdmin(admin.ModelAdmin):
    inlines = [SocialNetworkInline]


admin.site.register(ContactInfo, ContactInfoAdmin)