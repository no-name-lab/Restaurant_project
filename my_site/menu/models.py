from django.db import models
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField


class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=64)
    text = models.TextField()
    location = models.URLField()
    hotline = PhoneNumberField()

    def __str__(self):
        return f'{self.restaurant_name}'


class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    description_about = models.TextField()
    address = models.CharField(max_length=100)
    WORKING_DAYS_CHOICES = (
        ('ПН', 'ПН'),
        ('ВТ', 'ВТ'),
        ('СР', 'СР'),
        ('ЧТ', 'ЧТ'),
        ('ПТ', 'ПТ'),
        ('СБ', 'СБ'),
        ('ВС', 'ВС'),
    )
    working_days = MultiSelectField(choices=WORKING_DAYS_CHOICES, max_length=64, max_choices=6)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return f'about us {self.title}'


class AboutUsImage(models.Model):
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='about_us')
    images = models.ImageField(upload_to='about_us_img/')



class BestSellers(models.Model):
    best_name = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return f'best sellers {self.best_name}'


class BestsellerPhotos(models.Model):
    bestseller = models.ForeignKey(BestSellers, on_delete=models.CASCADE)
    photos = models.ImageField(upload_to='photo')


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.category_name}'


class Product(models.Model):
    name = models.CharField(max_length=200)
    product_image = models.ImageField(upload_to='product_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='foods')
    product_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name}'


class Extra(models.Model):
    extra_name = models.CharField(max_length=64)
    extra_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='price')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='extra')

    def __str__(self):
        return f'{self.extra_name}'


class Drinks(models.Model):
    drink_name = models.CharField(max_length=32)
    drink_price = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='drinks')

    def __str__(self):
        return f'{self.drink_name}'


class Menu(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="dishes")
    menu_name = models.CharField(max_length=255)
    menu_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.menu_name


class Interior(models.Model):
    interior_title = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.interior_title}'


class InteriorImages(models.Model):
    interior = models.ForeignKey(Interior, on_delete=models.CASCADE, related_name='interior_images')
    interior_images = models.ImageField(upload_to='interior_image/')


class ContactInfo(models.Model):
    contact_number = PhoneNumberField()
    email = models.CharField(max_length=64)
    contact_address = models.URLField()

    def __str__(self):
        return f'{self.contact_number}'


class SocialNetwork(models.Model):
    network_name = models.CharField(max_length=64)
    network_url = models.URLField()
    contact = models.ForeignKey(ContactInfo, on_delete=models.CASCADE, related_name='contact')
