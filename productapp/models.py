from django.db import models
from ecomapp.models import Category, SubCategory, Company
from userapp.models import User
import uuid
from django.db.models import Avg
from multiselectfield import MultiSelectField

from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
def image_dir(self, filepath):
    return f'product/{self.product.product_name}/{"product_name.jpg"}'


def default_profile_image():
    return f"image.png"


class Colors(models.Model):
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.color

    class Meta:
        verbose_name_plural = 'Colors'


class Sizes(models.Model):
    size = models.CharField(max_length=20)

    def __str__(self):
        return self.size

    class Meta:
        verbose_name_plural = 'Sizes'


class Product(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
    subcategory_name = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='product_subcategory')
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='product_company')
    product_name = models.CharField(max_length=264, blank=False, verbose_name='Product Name')
    product_quantity = models.IntegerField(blank=False, verbose_name='Quantity')
    product_price = models.IntegerField(blank=False, verbose_name='Price')
    product_discount = models.IntegerField(blank=False, verbose_name='Discount', help_text='%')
    product_new_price = models.IntegerField(verbose_name='New Price', help_text='Warning: Do not edit this field!!!',
                                            blank=True)
    product_sales = models.IntegerField(default=0, verbose_name='Bought Amount', blank=True, null=True)
    added_date = models.DateTimeField(verbose_name='Created At', auto_now_add=True)

    product_description = models.TextField(verbose_name='Description', blank=False)
    image = models.ImageField(upload_to='product', verbose_name='Image')
    MY_CHOICES = (('red', 'Red'),
                  ('blue', 'Blue'),
                  ('green', 'Green'),
                  ('yellow', 'Yellow'),
                  ('purple', 'Purple'))
    product_colors = models.ManyToManyField(Colors, verbose_name='Available Colors', blank=True)
    product_sizes = models.ManyToManyField(Sizes, verbose_name='Available Sizes', blank=True)

    product_slug = models.SlugField(max_length=256, blank=True)

    total_order = models.IntegerField(blank=True)

    @property
    def avg_rating(self):
        if self.product_ratings.all().count() > 0:
            return self.product_ratings.all().aggregate(Avg('product_rating'))['product_rating__avg']
        else:
            return 0

    @property
    def total_rating_count(self):
        if self.product_ratings.all().count() > 0:
            return self.product_ratings.all().count()
        else:
            return 0

    def save(self, *args, **kwargs):
        self.product_new_price = self.product_price - (self.product_price * self.product_discount) / 100
        self.product_slug = f"{self.product_name.replace(' ', '-').replace('/', '-').replace('(', '').replace(')', '')}-{uuid.uuid4()}"
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.product_name


class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_rating')
    rating = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    product_rating = models.IntegerField(verbose_name='Rating', blank=False, choices=rating)
    product_comment = models.TextField(verbose_name='Comment', blank=True)
    rating_date = models.DateTimeField(auto_now_add=True)


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image_product')
    product_image = models.ImageField(upload_to=image_dir, verbose_name='Product Images')

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name_plural = 'Product Images'


class Coupon(models.Model):
    coupon_code = models.CharField(max_length=15, verbose_name='Coupon Code', unique=True)
    discount_amount = models.IntegerField(verbose_name='Discounted Amount')
    is_active = models.BooleanField(verbose_name='Activate Coupon')

    def __str__(self):
        return self.coupon_code

# if not ProductImages:
#     @receiver(post_save, sender=Product)
#     def create_image(sender, instance, created, **kwargs):
#         if created:
#             ProductImages.objects.create(product=instance)

# @receiver(post_save, sender=Product)
# def save_image(sender, instance, **kwargs):
#     instance.image_product.save()


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_wishlist')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlist_product')
