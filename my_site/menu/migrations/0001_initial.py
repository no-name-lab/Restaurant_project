# Generated by Django 5.1.6 on 2025-02-22 10:51

import django.db.models.deletion
import multiselectfield.db.fields
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('title_ru', models.CharField(max_length=200, null=True)),
                ('title_ky', models.CharField(max_length=200, null=True)),
                ('description_about', models.TextField()),
                ('description_about_en', models.TextField(null=True)),
                ('description_about_ru', models.TextField(null=True)),
                ('description_about_ky', models.TextField(null=True)),
                ('address', models.CharField(max_length=100)),
                ('working_days', multiselectfield.db.fields.MultiSelectField(choices=[('ПН', 'ПН'), ('ВТ', 'ВТ'), ('СР', 'СР'), ('ЧТ', 'ЧТ'), ('ПТ', 'ПТ'), ('СБ', 'СБ'), ('ВС', 'ВС')], max_length=64)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='BestSellers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('best_name', models.CharField(max_length=300)),
                ('best_name_en', models.CharField(max_length=300, null=True)),
                ('best_name_ru', models.CharField(max_length=300, null=True)),
                ('best_name_ky', models.CharField(max_length=300, null=True)),
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('description_ky', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255, unique=True)),
                ('category_name_en', models.CharField(max_length=255, null=True, unique=True)),
                ('category_name_ru', models.CharField(max_length=255, null=True, unique=True)),
                ('category_name_ky', models.CharField(max_length=255, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.CharField(max_length=64)),
                ('contact_address', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Interior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interior_title', models.CharField(max_length=64)),
                ('interior_title_en', models.CharField(max_length=64, null=True)),
                ('interior_title_ru', models.CharField(max_length=64, null=True)),
                ('interior_title_ky', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=64)),
                ('restaurant_name_en', models.CharField(max_length=64, null=True)),
                ('restaurant_name_ru', models.CharField(max_length=64, null=True)),
                ('restaurant_name_ky', models.CharField(max_length=64, null=True)),
                ('text', models.TextField()),
                ('text_en', models.TextField(null=True)),
                ('text_ru', models.TextField(null=True)),
                ('text_ky', models.TextField(null=True)),
                ('location', models.URLField()),
                ('hotline', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='AboutUsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='about_us_img/')),
                ('about_us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.aboutus')),
            ],
        ),
        migrations.CreateModel(
            name='BestsellerPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photos', models.ImageField(upload_to='photo')),
                ('bestseller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.bestsellers')),
            ],
        ),
        migrations.CreateModel(
            name='InteriorImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interior_images', models.ImageField(upload_to='interior_image/')),
                ('interior', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interior_images', to='menu.interior')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=255)),
                ('menu_name_en', models.CharField(max_length=255, null=True)),
                ('menu_name_ru', models.CharField(max_length=255, null=True)),
                ('menu_name_ky', models.CharField(max_length=255, null=True)),
                ('menu_description', models.TextField(blank=True, null=True)),
                ('menu_description_en', models.TextField(blank=True, null=True)),
                ('menu_description_ru', models.TextField(blank=True, null=True)),
                ('menu_description_ky', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='menu.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('name_en', models.CharField(max_length=200, null=True)),
                ('name_ru', models.CharField(max_length=200, null=True)),
                ('name_ky', models.CharField(max_length=200, null=True)),
                ('product_image', models.ImageField(upload_to='product_images/')),
                ('product_description', models.TextField()),
                ('product_description_en', models.TextField(null=True)),
                ('product_description_ru', models.TextField(null=True)),
                ('product_description_ky', models.TextField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='menu.category')),
            ],
        ),
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_name', models.CharField(max_length=64)),
                ('extra_name_en', models.CharField(max_length=64, null=True)),
                ('extra_name_ru', models.CharField(max_length=64, null=True)),
                ('extra_name_ky', models.CharField(max_length=64, null=True)),
                ('extra_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extra', to='menu.product')),
            ],
        ),
        migrations.CreateModel(
            name='Drinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink_name', models.CharField(max_length=32)),
                ('drink_name_en', models.CharField(max_length=32, null=True)),
                ('drink_name_ru', models.CharField(max_length=32, null=True)),
                ('drink_name_ky', models.CharField(max_length=32, null=True)),
                ('drink_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drinks', to='menu.product')),
            ],
        ),
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network_name', models.CharField(max_length=64)),
                ('network_url', models.URLField()),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact', to='menu.contactinfo')),
            ],
        ),
    ]
