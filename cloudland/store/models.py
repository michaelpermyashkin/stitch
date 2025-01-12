from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.datetime_safe import datetime

from .utils import unique_slugify

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profile_picture = models.ImageField(upload_to='seller_profiles', help_text="Upload your profile picture for our about page", blank=True, null=True)
    bio_description = models.TextField(max_length=500, default="", help_text="Brief bio describing who you are and what you do")
    seller_full_name = models.CharField(max_length=50)
    seller_listing_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    date_added = models.DateField(auto_now_add=True)
    slug = models.SlugField(null=True, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.seller_listing_name


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=30, help_text="Limit 30 characters")
    slug = models.SlugField(unique=True, null=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ManyToManyField(Category, help_text="Hold down “Control”, or “Command” on a Mac, to select more than one.")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=6, decimal_places=2)
    description_short = models.TextField(max_length=100, default="", help_text="Limit 100 characters: Brief discription of the item")
    description_full = models.TextField(max_length=1000, default="", help_text="Your full item description when item details are viewed")
    product_image = models.ImageField(upload_to='product_images', help_text="There are no image size restrictions, but sqaure images will always render without any cropping.")
    date_listed = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(help_text="Quantity available - Default 1", default=1)
    total_purchases = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.product_name

    def save(self, **kwargs):
        slug_str = "%s" % (self.product_name) 
        unique_slugify(self, slug_str) 
        super(Product, self).save(**kwargs)


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.PositiveIntegerField(default=5)
    subject = models.CharField(max_length=75, null=True, blank=True)
    comment = models.TextField(max_length=500, null=True, blank=True)
    timestamp = models.DateField(auto_now_add=True)